# Generated from tiny.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .tinyParser import tinyParser
else:
    from tinyParser import tinyParser

# This class defines a complete generic visitor for a parse tree produced by tinyParser.

class tinyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by tinyParser#program.
    def visitProgram(self, ctx:tinyParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinyParser#fun_head.
    def visitFun_head(self, ctx:tinyParser.Fun_headContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinyParser#fun.
    def visitFun(self, ctx:tinyParser.FunContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinyParser#id_list.
    def visitId_list(self, ctx:tinyParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinyParser#exp_list.
    def visitExp_list(self, ctx:tinyParser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinyParser#stm.
    def visitStm(self, ctx:tinyParser.StmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinyParser#else.
    def visitElse(self, ctx:tinyParser.ElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinyParser#exp.
    def visitExp(self, ctx:tinyParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinyParser#fun_call.
    def visitFun_call(self, ctx:tinyParser.Fun_callContext):
        return self.visitChildren(ctx)



del tinyParser