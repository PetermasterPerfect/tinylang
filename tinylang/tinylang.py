from antlr4 import *
from time import *
from tinylang.antlr_gen.tinyLexer import tinyLexer
from tinylang.antlr_gen.tinyParser import tinyParser
from tinylang.ast_builder import TinyAstBuilder
from tinylang.cfg import FunCfg
from tinylang.monotone_framework import *
from tinylang.dominators import *
from tinylang.compiler import *
from ctypes import CFUNCTYPE, c_double
import llvmlite.binding as llvm
#java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -no-listener -visitor tiny.g4 

def time_test_monotone_framework(ast):
    for f in ast.functions:
        fun_cfg = FunCfg(f)
        for analysis in [AvailableExpressionsAnalysis, LiveVariablesAnalysis, ReachingDefinitionsAnalysis, VeryBusyExpressionsAnalysis]:
            monotone = MDFAF(fun_cfg, analysis(fun_cfg))
            s=time()
            monotone.fixed_point_solve()
            print('fixed point: ', time()-s)
            s=time()
            monotone.chaotic_solve()
            print('chaotic: ', time()-s)
            s=time()
            sol = monotone.simple_worklist_solve()
            print('simple worklist: ', time()-s)
            print('-------')

def test_monotone_framework(ast):
    def check(list):
        return all(i == list[0] for i in list)
    
    for f in ast.functions:
            fun_cfg = FunCfg(f)
            for analysis in [VeryBusyExpressionsAnalysis]:#, LiveVariablesAnalysis, ReachingDefinitionsAnalysis, VeryBusyExpressionsAnalysis]:
                monotone = MDFAF(fun_cfg, analysis(fun_cfg))
                sol = []
                sol.append(monotone.fixed_point_solve())
                print('fixed point: \n', sol[-1])
                #print([f'{x} - {x.ast_node.label()}' for x in sol[-1]])
                sol.append(monotone.chaotic_solve())
                print('chaotic: \n', sol[-1])
                sol.append(monotone.simple_worklist_solve())
                print('simple worklist: \n', sol[-1])
                print('-------')

def test_dominators(ast):
    for f in ast.functions:
        fun_cfg = FunCfg(f)
        #fun_cfg.dump_2_dot()
        dom_tree = DominatorsTree(fun_cfg)
        print(dom_tree.idoms)
        dom_front = DominanceFrontier(fun_cfg)
        for x in dom_front.dom_frontier:
            print(x.ast_node.label())
            for y in dom_front.dom_frontier[x]:
                print('\t'+y.ast_node.label())

def create_execution_engine():
    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    backing_mod = llvm.parse_assembly("")
    engine = llvm.create_mcjit_compiler(backing_mod, target_machine)
    return engine

def compile_ir(engine, llvm_ir):
    mod = llvm.parse_assembly(llvm_ir)
    mod.verify()
    engine.add_module(mod)
    engine.finalize_object()
    engine.run_static_constructors()
    return mod


def main(argv):
    if len(argv)<2:
        print('usage: tinylang.py <script_name>\n')
        return
    input_stream = FileStream(argv[1])
    lexer = tinyLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = tinyParser(stream)
    tree = parser.program()
    ast_builder = TinyAstBuilder()
    ast = ast_builder.visit(tree)
    module = ir.Module(name=argv[1])
    states = []
    names = {x.name for x in ast.functions}
    if len(names) < len(ast.functions):
        print("Error: function name duplicated")
        return
    for f in ast.functions:
        states.append(FunCompileState(f, module))

    for i in range(len(ast.functions)):
        ast.functions[i].compile(states[i])
    print(module)
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()
    engine = create_execution_engine()
    mod = compile_ir(engine, str(module))
    func_ptr = engine.get_function_address("main")
    cfunc = CFUNCTYPE(c_double, c_double)(func_ptr)
    res = cfunc(10)
    print("main(...) =", res)
