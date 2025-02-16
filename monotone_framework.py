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

class LiveVariablesAnalysis:
    def __init__(self, cfg):
        self.lattice_bottom = set()
        self.bound = cfg.exit_stm


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


    def constraints_from_cfg(self, nodes):
        fun_constraints = dict()
        for node in nodes:
            print(node.ast_node)
            if node == self.bound:
                fun_constraints[node] = LiveVariablesAnalysis.return_f
            elif type(node.ast_node) is AssignAstNode:
                fun_constraints[node] = LiveVariablesAnalysis.assignment_f
            else:
                fun_constraints[node] = LiveVariablesAnalysis.exp_f
        return fun_constraints



class MDFAF: # monotone data flow analysis framework
    def __init__(self, graph, model_analysis):
        self.function_vars = graph.ast_node.vars
        self.cfg = graph
        self.nodes = list(cfg_dfs(graph.start_stm))
        self.model_analysis = model_analysis
        self.fun_constraints = self.model_analysis.constraints_from_cfg(self.nodes)


    def solve(self):
        sol = dict(zip(self.nodes, [self.model_analysis.lattice_bottom for x in self.fun_constraints]))
        f = [ self.fun_constraints[e](sol, self.nodes[i]) for i, e in enumerate(self.fun_constraints) ]
        while sol != f:
            for i, e in enumerate(self.fun_constraints):
                sol[e] = self.fun_constraints[e](sol, e)
            f = dict(zip(self.nodes, [ self.fun_constraints[e](sol, self.nodes[i]) for i, e in enumerate(self.fun_constraints) ]))
        return sol
