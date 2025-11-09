from ast_builder import *
from llvmlite import ir

#TODO: make cfg dot graph prettier
def flatten_list(l):
    ret = []
    for i in l:
        if type(i) is list:
            ret += flatten_list(i)
        else:
            ret.append(i)
    return ret

def ast_to_cfg(stms):
    limit = []
    old = []
    for i in range(len(stms)):
        stm = stms[i]
        if type(stm) is IfAstNode:
            cond_cfg = StmCfg(stm.cond)
            cond_cfg.annots = {'then':False, 'else':True}
            if i == 0:
                limit.append(cond_cfg)
            if then_limit := ast_to_cfg(stm.then):
                cond_cfg.annots['then'] = True
                branches = [then_limit[1]]
                cond_cfg.successors.append(then_limit[0])
            if stm.els:
                if else_limit := ast_to_cfg(stm.els):
                    cond_cfg.annots['else'] = True
                    branches.append(else_limit[1])
                    cond_cfg.successors.append(else_limit[0])
            else:
                branches.append(cond_cfg)
            for o in flatten_list(old):
                o.successors.append(cond_cfg)
            old = []
            for b in branches:
                old.append(b)
        elif type(stm) is WhileAstNode:
            cond_cfg = StmCfg(stm.cond)
            cond_cfg.annots = {'then':False, 'else':True}
            if i == 0:
                limit.append(cond_cfg)
            if body_limit := ast_to_cfg(stm.body):
                cond_cfg.annots['then'] = True
                cond_cfg.successors.append(body_limit[0])
                if type(body_limit[1]) is not list:
                    body_limit[1].successors.append(cond_cfg)
                else:
                    for j in body_limit[1]:
                        j.successors.append(cond_cfg)
            for o in flatten_list(old):
                o.successors.append(cond_cfg)

            old = [cond_cfg]
        else:
            buf = StmCfg(stm)
            for o in flatten_list(old):
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
 

def reverse_dfs(node, tab=set()):
    tab.add(node)
    for s in node.predecessor:
        print(f'{node} -> {s}')
        if s not in tab:
            reverse_dfs(s, tab)
    return tab 



def cfg_dfs(node, tab=set()):
    if node not in tab:
        tab.add(node)
    else:
        return tab
    for s in node.successors:
        tab|=cfg_dfs(s, tab)
    return tab 


class FunCfg:
    def __init__(self, fun_ast_node):
        self.ast_node = fun_ast_node
        if limit := ast_to_cfg(fun_ast_node.stms):
            ret_node = StmCfg(fun_ast_node.ret)
            if type(limit[1]) is not list:
                limit[1].successors.append(ret_node)
            else:
                for i in flatten_list(limit[1]):
                    """
                    Solution with flatten_list is naive. 
                    TODO: limit[1] should contain list of predecessors of return node.
                    Now it can containts list of list(when last instuctions is conditional instruction with nested conditional instructions).
                    Thats why I solve this problem with flattening but still ast_to_cfg returns ugly list
                    e.g.
                    foo() {
                        var x, y;
                        if(1) {
                            if(2) { x=2; } 
                            else { y=3; }
                        } else {
                            if(x==2) { y=2; }
                            else { x=3; }
                        }
                        return 0;
                    }
                    """
                    i.successors.append(ret_node)
            self.start_stm = limit[0]
            self.exit_stm = ret_node
        else:
            self.start_stm = None
            self.exit_stm = StmCfg(fun_ast_node.ret)

        if self.start_stm:
            self.reversal_mapping = self.reverse_cfg()


    def compile_to_llvm_ir():
        double = ir.DoubleType()
        func_type = ir.FunctionType(double, (double for x in self.ast_node.args))
        module = ir.Module(name='changeit')
        func_ir = ir.Function(module, func_type, self.ast_node.name)



    def reverse_cfg(self):
        def do_reversing(node, reversed_nodes=dict()):
            for n in node.successors:
                if n in reversed_nodes:
                    reversed_nodes[n].add(node)
                    n.predecessors.add(node)
                else:
                    reversed_nodes[n] = {node}
                    n.predecessors = {node}
                    reversed_nodes = do_reversing(n, reversed_nodes)
            return reversed_nodes


        ret = do_reversing(self.start_stm)
        if self.start_stm not in ret:
            ret[self.start_stm] = set()
            self.start_stm.predecessors = set()
        return ret


    def dump_2_dot(self):
        print('digraph cfg{')
        if self.start_stm:
            self.start_stm.dump_2_dot(f'{self.start_stm} -> ')
        else:
            self.exit_stm.dump_2_dot(f'{self.exit_stm} -> ')
        print('}')


    def compile(self, state):
        for s in self.ast_node.stms:
            s.compile(state)
        self.ast_node.ret.compile(state)


class StmCfg:
    def __init__(self, node):
        self.ast_node = node
        self.successors = []


    def dump_2_dot(self, st=None, tab=None):
        if st is None:
            st = ''
        if tab is None:
            tab = []

        if self in tab:
            return
        else:
            tab.append(self)

        print(f'{self} [label="{self.ast_node.label()}"]')
        for s in self.successors:
            print(f'{st}{s}')
            s.dump_2_dot(f'{s} -> ', tab)
