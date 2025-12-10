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
import argparse
#java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -no-listener -visitor tiny.g4 

def time_measure_monotone_framework(ast):
    for f in ast.functions:
        fun_cfg = FunCfg(f)
        print('Function ', fun_cfg.ast_node.name)
        for analysis in [AvailableExpressionsAnalysis, LiveVariablesAnalysis, ReachingDefinitionsAnalysis, VeryBusyExpressionsAnalysis]:
            print('Analysis type: ', analysis)
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
        print('########\n')

def run_monotone_framework(ast):
    for f in ast.functions:
            fun_cfg = FunCfg(f)
            for analysis in [VeryBusyExpressionsAnalysis, LiveVariablesAnalysis, ReachingDefinitionsAnalysis, VeryBusyExpressionsAnalysis]:
                print('Analysis type: ', analysis)
                monotone = MDFAF(fun_cfg, analysis(fun_cfg))
                sol = monotone.simple_worklist_solve()
                print('simple worklist: \n', [f'{x} - {sol[x]}' for x in sol])
                print('-------')

def test_dominators(ast):
    for f in ast.functions:
        fun_cfg = FunCfg(f)
        fun_cfg.dump_2_dot()
        dom_tree = DominatorsTree(fun_cfg)
        print(dom_tree.order)
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

def compile_and_execute(ast, module_name="module", print_module=False):
    module = ir.Module(name=module_name)
    states = []
    names = {x.name for x in ast.functions}
    if len(names) < len(ast.functions):
        print("Error: function name duplicated")
        return

    for f in ast.functions:
        states.append(FunCompileState(f, module))

    for i in range(len(ast.functions)):
        ast.functions[i].compile(states[i])

    if print_module:
        print(module)

    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()
    engine = create_execution_engine()
    mod = compile_ir(engine, str(module))

    func_ptr = engine.get_function_address("main")
    cfunc = CFUNCTYPE(c_double, c_double)(func_ptr)
    res = cfunc(1)
    print("main(...) =", res)


def main():
    parser = argparse.ArgumentParser(description="TinyLang toolchain")
    subparsers = parser.add_subparsers(dest="mode", required=True)

    compile_parser = subparsers.add_parser("compile", help="Compile and execute")
    compile_parser.add_argument("file", help="Input TinyLang file")
    compile_parser.add_argument(
        "--print-module",
        action="store_true",
        help="Print generated LLVM IR module"
    )

    mono_parser = subparsers.add_parser("monotone", help="Run monotone framework")
    mono_parser.add_argument("file", help="Input TinyLang file")

    time_parser = subparsers.add_parser("time", help="Benchmark monotone solvers")
    time_parser.add_argument("file", help="Input TinyLang file")

    args = parser.parse_args()

    input_stream = FileStream(args.file)
    lexer = tinyLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser_ = tinyParser(stream)
    tree = parser_.program()

    ast_builder = TinyAstBuilder()
    ast = ast_builder.visit(tree)

    if args.mode == "compile":
        compile_and_execute(
            ast,
            module_name=args.file,
            print_module=args.print_module
        )

    elif args.mode == "monotone":
        run_monotone_framework(ast)

    elif args.mode == "time":
        time_measure_monotone_framework(ast)

