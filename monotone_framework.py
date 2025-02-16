import types
from cfg import *
from ast import *

def cfg_dfs(node, tab=set()):
    if node not in tab:
        tab.add(node)
    else:
        return tab
    for s in node.successors:
        tab|=cfg_dfs(s, tab)
    return tab 

def exp_f(constraints, node):
    ret = set()
    for s in node.successors:
        ret |= constraints[s]
    return ret | node.ast_node.get_used_vars()

def assignment_f(constraints, node):
    ret = set()
    for s in node.successors:
        ret |= constraints[s]
    return ret - {node.ast_node.name} | node.ast_node.exp.get_used_vars()

def return_f(constraints, node):
    return node.ast_node.get_used_vars()

def show(sol):
    print(dict(zip([x.ast_node for x in sol], [sol[x] for x in sol])))


class MDFAF: # monotone data flow analysis framework
    def __init__(self, graph):
        self.function_vars = graph.ast_node.vars
        self.cfg = graph
        self.nodes = list(cfg_dfs(graph.start_stm))
        self.node_to_constraints()


    def solve(self):
        sol = dict(zip(self.nodes, [set() for x in self.fun_constraints]))
        f = [ self.fun_constraints[e](sol, self.nodes[i]) for i, e in enumerate(self.fun_constraints) ]
        while sol != f:
            for i, e in enumerate(self.fun_constraints):
                sol[e] = self.fun_constraints[e](sol, e)
            f = dict(zip(self.nodes, [ self.fun_constraints[e](sol, self.nodes[i]) for i, e in enumerate(self.fun_constraints) ]))
        return sol
    

    def node_to_constraints(self):
        self.fun_constraints = dict()
        for node in self.nodes:
            print(node.ast_node)
            if node == self.cfg.exit_stm:
                self.fun_constraints[node] = return_f
            elif type(node.ast_node) is AssignAstNode:
                self.fun_constraints[node] = assignment_f
            else:
                self.fun_constraints[node] = exp_f
