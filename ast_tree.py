from tinyVisitor import *
from tinyParser import tinyParser
import pdb


class ProgramAstNode:
    def __init__(self):
        self.functions = []


class FunAstNode():
    def __init__(self, n, a, v, s, r):
        self.name = n
        self.args = a
        self.vars = v
        self.stms = s
        self.ret = r


class AssignAstNode():
    def __init__(self, n, v):
        self.name = n
        self.value = v


class OutputAstNode():
    def __init__(self, e):
        self.exp = e


class IfAstNode():
    def __init__(self, c, t, e):
        self.cond = c
        self.then = t
        self.els = e


class WhileAstNode():
    def __init__(self, c, b):
        self.cond = c
        self.body = b


class ExpAstNode():
    def __init__(self, s, o=None):
        self.sub_exps = s
        self.op = o


class NumAstNode():
    def __init__(self, v):
        self.value = v


class IdAstNode():
    def __init__(self, n):
        self.name = n


class FunCallAstNode():
    def __init__(self, n, p):
        self.name = n
        self.params = p


class InputAstNode():
    pass

def token_to_operator(ctx):
    if ctx.ADD():
        return '+'
    elif ctx.SUB():
        return '-'
    elif ctx.MUL():
        return '*'
    elif ctx.DIV():
        return '/'
    elif ctx.EQ():
        return '=='
    elif ctx.GR():
        return '>'


class TinyAstBuilder(tinyVisitor):


    def visitProgram(self, ctx:tinyParser.ProgramContext):
        buf = [self.visit(x) for x in ctx.children]
        for i in buf:
            print(i)
        return buf
    

    def visitFun_head(self, ctx:tinyParser.Fun_headContext):
        name = ctx.ID().getText()
        args = [x.getText() for x in ctx.id_list().ID()] if ctx.id_list() else None
        return name, args


    def visitFun(self, ctx:tinyParser.FunContext):
        name, args = self.visit(ctx.fun_head())
        var = [x.getText for x in ctx.id_list().ID()] if ctx.VAR() else None
        stms = [self.visit(x) for x in ctx.stm()]
        ret = self.visit(ctx.exp())
        return FunAstNode(name, args, var, stms, ret);


    def visitId_list(self, ctx:tinyParser.Id_listContext):
        return [self.x.getText() for x in ctx.children]


    def visitExp_list(self, ctx:tinyParser.Exp_listContext):
        return [self.visit(x) for x in ctx.children]

    def visitElse(self, ctx:tinyParser.ElseContext):
        else_block = [self.visit(x) for x in ctx.stm()]
        return else_block


    def visitStm(self, ctx:tinyParser.StmContext):
        if ctx.ID():
            return AssignAstNode(ctx.ID().getText(), self.visit(ctx.exp()))
        elif ctx.OUTPUT():
            return OutputAstNode(self.visit(ctx.exp()))
        elif ctx.IF():
            cond = self.visit(ctx.exp())
            then_block = [self.visit(x) for x in ctx.stm()]
            if ctx.else_():
                else_block = self.visit(ctx.else_())
                return IfAstNode(cond, then_block, else_block)
            else:
                return IfAstNode(cond, then_block, [])
        elif ctx.WHILE():
            cond = self.visit(ctx.exp())
            loop_block = [self.visit(x) for x in ctx.stm()]
            return WhileAstNode(cond, loop_block)
            

    def visitFun_call(self, ctx:tinyParser.Fun_callContext):
        name = ctx.ID().getText()
        params = self.visit(ctx.exp_list())
        return FunCallAstNode(name, params)


    def visitExp(self, ctx:tinyParser.ExpContext):
        if ctx.INT():
            return NumAstNode(int(ctx.INT().getText()))
        elif ctx.ID():
            return IdAstNode(ctx.ID().getText())
        elif ctx.INPUT():
            return InputAstNode()
        elif fun_call_ctx := ctx.fun_call():
            return self.visit(fun_call_ctx)
        else:
            exp = ctx.exp()
            sub_exp = [self.visit(x) for x in exp]
            return ExpAstNode(sub_exp, token_to_operator(ctx))


