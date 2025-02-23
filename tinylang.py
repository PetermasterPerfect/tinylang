from antlr4 import *
from tinyLexer import tinyLexer
from tinyParser import tinyParser
from ast import TinyAstBuilder
from cfg import FunCfg
from monotone_framework import *
import sys

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
        a = AvailableExpressionsAnalysis(fun_cfg)
        ins = MDFAF(fun_cfg, a)
        fun_cfg.print_all()
        sol = ins.solve()

if __name__ == "__main__":
    main(sys.argv)
