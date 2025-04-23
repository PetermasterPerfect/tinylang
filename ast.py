from tinyVisitor import *
from tinyParser import tinyParser
from random import randint
import pdb


class DotGraphElement:
    def __init__(self, name, label, sub_chain=[]):
        self.name = name
        self.id = f'{name}_{randint(1, 1000000)}' # TODO: list of chosen ids as static variable so new id wont be the same
        self.label = label
        if type(sub_chain) is not list:
            self.sub_chain = [sub_chain]
        else:
            self.sub_chain = sub_chain

    
    def print_dot(self):
        if self.sub_chain:
            for i in self.sub_chain:
                print(f'{self.id} -> {i}')
        if self.label in ['then', 'else']:
            print(f'{self.id} [label="{self.label}" style=filled, fillcolor="blue:green", gradientangle=270]')
        else:
            print(f'{self.id} [label="{self.label}"]')


class AstNode:
    def dump_2_dot():
        return None


    def get_used_vars(self):
        return set()


class ProgramAstNode(AstNode):
    def __init__(self, fs):
        self.functions = fs


    def dump_2_dot(self):
        print('digraph ast {')
        for f in self.functions:
            f.dump_2_dot()
        print('}')


class FunAstNode(AstNode):
    def __init__(self, n, a, v, s, r):
        self.name = n
        self.args = a
        self.vars = v
        self.stms = s
        self.ret = r


    def dump_2_dot(self):
        sub_stms = [x.dump_2_dot() for x in self.stms]
        label = [x.label for x in sub_stms]
        sub_chain = [x.id for x in sub_stms]

        sub_ret = self.ret.dump_2_dot()
        return_node = DotGraphElement('ret', f'return {sub_ret.label}', sub_ret.id)

        header_label = f'{self.name}({", ".join(self.args)})\\n'
        header_label += f'var {", ".join(self.vars)}'
        header_node = DotGraphElement('fun_header', header_label, [return_node.id]+sub_chain)
        header_node.print_dot()
        return_node.print_dot()
        

class AssignAstNode(AstNode):
    def __init__(self, n, v):
        self.name = n
        self.exp = v


    def label(self):
        return f'{self.name}={self.exp.label()}'
    

    def dump_2_dot(self):
        sub = self.exp.dump_2_dot()
        dot = DotGraphElement('assignment', self.label(), sub.id)
        dot.print_dot()
        return dot


class OutputAstNode(AstNode):
    def __init__(self, e):
        self.exp = e

   
    def label(self):
        return f'output {self.exp.label()}'
    
    def dump_2_dot(self):
        exp = self.exp.dump_2_dot()
        dot = DotGraphElement('output', self.label(), exp.id)
        dot.print_dot()
        return dot

    
    def get_used_vars(self):
        return self.exp.get_used_vars()

class IfAstNode(AstNode):
    def __init__(self, c, t, e):
        self.cond = c
        self.then = t
        self.els = e

    
    def label(self):
        return f'if {self.cond.label()}'


    def dump_2_dot(self):
        cond_node = self.cond.dump_2_dot()
        then_nodes = [x.dump_2_dot() for x in self.then]
        then_sub_chain = [x.id for x in then_nodes]
        then_node = DotGraphElement('then', 'then', then_sub_chain)
        if self.els:
            else_nodes = [x.dump_2_dot() for x in self.els]
            else_sub_chain = [x.id for x in else_nodes]
            else_node = DotGraphElement('else', 'else', else_sub_chain)
            sub_chain = [cond_node.id, then_node.id, else_node.id]
        else:
            sub_chain = [cond_node.id, then_node.id]
        if_node = DotGraphElement('if', self.label(), sub_chain)
        if_node.print_dot()
        then_node.print_dot()
        if self.els:
            else_node.print_dot()
        return if_node
        

class WhileAstNode(AstNode):
    def __init__(self, c, b):
        self.cond = c
        self.body = b


    def label(self):
        return f'while {self.cond.label()}'


    def dump_2_dot(self):
        cond_node = self.cond.dump_2_dot()
        body_nodes = [x.dump_2_dot() for x in self.body]
        sub_chain = [x.id for x in body_nodes]
        loop_node = DotGraphElement('loop', self.label(), [cond_node.id]+sub_chain)
        loop_node.print_dot()
        return loop_node


class ExpAstNode(AstNode):
    def __init__(self, s, o=None):
        self.sub_exps = s
        self.op = o

    
    def label(self):
        return self.op.join([x.label() for x in self.sub_exps]) if self.op else self.sub_exps[0].label()


    def dump_2_dot(self):
        sub_exp = [x.dump_2_dot() for x in self.sub_exps]
        sub_chain = [x.id for x in sub_exp]
        dot = DotGraphElement('exp', self.label(), sub_chain)
        dot.print_dot()
        return dot
        
        
    def get_used_vars(self):
        ret_vars = set()
        for i in self.sub_exps:
            ret_vars = ret_vars.union(i.get_used_vars())
        return ret_vars


    def exps(self):
        ret = {str(self)}
        for e in self.sub_exps:
            if type(e) is ExpAstNode:
                ret |= e.exps()
        return ret


    def __str__(self):
        return self.op.join([str(x) for x in self.sub_exps]) if self.op else str(self.sub_exps[0])

 
class NumAstNode(AstNode):
    def __init__(self, v):
        self.value = v


    def label(self):
        return f'{self.value}'
        

    def dump_2_dot(self):
        dot = DotGraphElement('num',str(self.value))
        dot.print_dot()
        return dot


    def __str__(self):
        return str(self.value)


class IdAstNode(AstNode):
    def __init__(self, n):
        self.name = n


    def label(self):
        return f'{self.name}'


    def dump_2_dot(self):
        dot = DotGraphElement('id', self.name)
        dot.print_dot()
        return dot


    def get_used_vars(self):
        return {self.name}


    def exps(self):
        return set()


    def __str__(self):
        return self.name


class FunCallAstNode(AstNode):
    def __init__(self, n, p):
        self.name = n
        self.params = p


    def label(self):
        args = ', '.join([x.label() for x in self.params])
        return f'{name}({args})'


    def dump_2_dot(self):
        sub_exp = [x.dump_2_dot() for x in self.params]
        sub_chain = [x.id for x in sub_exp]
        dot = DotGraphElement('fun', self.label(), sub_chain)
        dot.print_dot()
        return dot


class InputAstNode(AstNode):
    def dump_2_dot(self):
        dot = DotGraphElement('input', f'input')
        dot.print_dot()
        return dot

    
    def label(self):
        return 'input'

    
    def exps(self):
        return {'input'}


    def get_used_vars(self):
        return set()


    def __str__(self):
        return 'input'


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
        funs = [self.visit(x) for x in ctx.children]
        return ProgramAstNode(funs)
    

    def visitFun_head(self, ctx:tinyParser.Fun_headContext):
        name = ctx.ID().getText()
        args = [x.getText() for x in ctx.id_list().ID()] if ctx.id_list() else []
        return name, args


    def visitFun(self, ctx:tinyParser.FunContext):
        name, args = self.visit(ctx.fun_head())
        var = [x.getText() for x in ctx.id_list().ID()] if ctx.VAR() else []
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


