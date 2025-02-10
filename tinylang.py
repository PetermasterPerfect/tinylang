from antlr4 import *
from tinyLexer import tinyLexer
from tinyParser import tinyParser
from ast_tree import TinyAstBuilder
import sys

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = tinyLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = tinyParser(stream)
    tree = parser.program()
    ast_builder = TinyAstBuilder()
    ast_builder.visit(tree)

if __name__ == "__main__":
    main(sys.argv)
