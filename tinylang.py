from antlr4 import *
from time import *
from tinyLexer import tinyLexer
from tinyParser import tinyParser
from ast import TinyAstBuilder
from cfg import FunCfg
from monotone_framework import *
from dominators import *
import sys
from compiler import *

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
            s=time()
            sol = monotone.propagation_worklist_solve()
            print('propagation worklist: ', time()-s)
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
                sol.append(monotone.propagation_worklist_solve())
                print('propagation worklist: \n', sol[-1])
                print(check(sol))
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

def main(argv):
    if len(argv)<2:
        print('usage: tinylang.py <script_name>\n')
        sys.exit(3)
    input_stream = FileStream(argv[1])
    lexer = tinyLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = tinyParser(stream)
    tree = parser.program()
    ast_builder = TinyAstBuilder()
    ast = ast_builder.visit(tree)

    module = ir.Module(name=argv[1])
    for f in ast.functions:
        fun_cfg = FunCfg(f)
        fun_cfg.dump_2_dot()
        #f_comp = FuncCompiler(module, fun_cfg)
        #f_comp.compile_function()
    print(module)


if __name__ == "__main__":
    main(sys.argv)
