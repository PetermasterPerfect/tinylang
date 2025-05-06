from antlr4 import *
from tinyLexer import tinyLexer
from tinyParser import tinyParser
from ast import TinyAstBuilder
from cfg import FunCfg
from monotone_framework import *
from dominators import *
import sys

def test_monotone_framework(ast):
    for f in ast.functions:
            fun_cfg = FunCfg(f)
            for analysis in [AvailableExpressionsAnalysis, LiveVariablesAnalysis, ReachingDefinitionsAnalysis, VeryBusyExpressionsAnalysis]:
                monotone = MDFAF(fun_cfg, analysis(fun_cfg))
                sol = monotone.fixed_point_solve()
                print(sol)
                sol = monotone.chaotic_iteration()
                print(sol)
                sol = monotone.simple_worklist_solve()
                print(sol)
                print('-------')

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

if __name__ == "__main__":
    main(sys.argv)
