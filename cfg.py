from ast import *



def ast_to_cfg(stms):
    limit = []
    old = []
    for i in range(len(stms)):
        stm = stms[i]
        if type(stm) is IfAstNode:
            cond_cfg = StmCfg(stm.cond)
            if i == 0:
                limit.append(cond_cfg)
            if then_limit := ast_to_cfg(stm.then):
                branches = [then_limit[1]]
                cond_cfg.successors.append(then_limit[0])
            if stm.els:
                if else_limit := ast_to_cfg(stm.els):
                    branches.append(else_limit[1])
                    cond_cfg.successors.append(else_limit[0])
            else:
                branches.append(cond_cfg)
            for o in old:
                o.successors.append(cond_cfg)
            #print(cond_cfg.successors)
            old = []
            for b in branches:
                old.append(b)
        elif type(stm) is WhileAstNode:
            cond_cfg = StmCfg(stm.cond)
            if i == 0:
                limit.append(cond_cfg)
            if body_limit := ast_to_cfg(stm.body):
                cond_cfg.successors.append(body_limit[0])
                if type(body_limit[1]) is not list:
                    body_limit[1].successors.append(cond_cfg)
                else:
                    for j in body_limit[1]:
                        j.successors.append(cond_cfg)
            for o in old:
                o.successors.append(cond_cfg)

            old = [cond_cfg]
        else:
            buf = StmCfg(stm.exp)
            for o in old:
                o.successors.append(buf)
            old = [buf]
        if i == 0 and not limit:
            limit+=old
        if i == len(stms)-1:
            if len(old)>1:
                limit += [old]
            else:
                limit += old
    return limit
 

class FunCfg:
    def __init__(self, fun_ast_node):
        self.ast_node = fun_ast_node
        if limit := ast_to_cfg(fun_ast_node.stms):
            ret_node = StmCfg(fun_ast_node.ret)
            if type(limit[1]) is not list:
                limit[1].successors.append(ret_node)
            else:
                for i in limit[1]:
                    i.successors.append(ret_node)
            self.start_stm = limit[0]
        else:
            self.start_stm = None


    def print_all(self):
        print('digraph cfg{')
        self.start_stm.print(f'{self.start_stm} -> ')
        print('}')


class StmCfg:
    def __init__(self, node):
        self.ast_node = node
        self.successors = []


    def print(self, st='', tab=[]):
        if self in tab:
            return
        else:
            tab.append(self)

        for s in self.successors:
            print(f'{st}{s}')
            s.print(f'{s} -> ')
