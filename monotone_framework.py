import types
from cfg import *
from ast import *


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


    def bound_f(constraints, node):
        return node.ast_node.get_used_vars()


    def constraints_from_cfg(self, nodes):
        fun_constraints = dict()
        for node in nodes:
            if node == self.bound:
                fun_constraints[node] = LiveVariablesAnalysis.bound_f
            elif type(node.ast_node) is AssignAstNode:
                fun_constraints[node] = LiveVariablesAnalysis.assignment_f
            else:
                fun_constraints[node] = LiveVariablesAnalysis.exp_f
        return fun_constraints


def exclude_substr_from_set(sub, base):
    ret = set()
    for i in base:
        if sub not in i:
            ret.add(i)
    return ret

class AvailableExpressionsAnalysis:
    def __init__(self, cfg):
        AvailableExpressionsAnalysis.reversed_cfg = reverse_cfg(cfg)
        self.bound = None # cfg.start_stm
        self.lattice_bottom = self.extract_expressions_nodes()


    def extract_expressions_nodes(self):
        exp_nodes = set()
        for k in AvailableExpressionsAnalysis.reversed_cfg:
            for node in AvailableExpressionsAnalysis.reversed_cfg[k]:
                if type(node.ast_node) is ExpAstNode:
                    exp_nodes.add(node.ast_node)
                elif type(node.ast_node) in [AssignAstNode, OutputAstNode]:
                    exp_nodes.add(node.ast_node.exp)
        ret = set()
        for e in exp_nodes:
            ret |= e.exps()
        return ret


    def exp_f(constraints, node):
        ret = set()
        for p in AvailableExpressionsAnalysis.reversed_cfg[node]:
            current_const = constraints[p]
            if len(ret) == 0:
                ret = current_const.copy()
            else:
                ret &= current_const
        if type(node.ast_node) is ExpAstNode:
            ret |= node.ast_node.exps() 
        return ret


    def assignment_f(constraints, node):
        ret = set()
        var_name = node.ast_node.name
        for p in AvailableExpressionsAnalysis.reversed_cfg[node]:
            current_const = exclude_substr_from_set(var_name, constraints[p])
            if len(ret) == 0:
                ret = current_const.copy()
            else:
                ret &= current_const
        exps = exclude_substr_from_set(var_name, node.ast_node.exp.exps())
        ret |= exps
        return ret


    def bound_f(constraints, node):
        return set()


    def constraints_from_cfg(self, nodes):
        fun_constraints = dict()
        for node in nodes:
            if node == self.bound:
                fun_constraints[node] = AvailableExpressionsAnalysis.bound_f
            elif type(node.ast_node) is AssignAstNode:
                fun_constraints[node] = AvailableExpressionsAnalysis.assignment_f
            else:
                fun_constraints[node] = AvailableExpressionsAnalysis.exp_f
        return fun_constraints


class MDFAF: # monotone data flow analysis framework
    def __init__(self, graph, model_analysis):
        self.function_vars = graph.ast_node.vars
        self.cfg = graph
        self.nodes = list(cfg_dfs(graph.start_stm))
        self.model_analysis = model_analysis
        self.fun_constraints = self.model_analysis.constraints_from_cfg(self.nodes)


    def solve(self):
        sol = dict(zip(self.nodes, [self.model_analysis.lattice_bottom.copy() for x in self.fun_constraints]))
        f = dict(zip(self.nodes, [ self.fun_constraints[e](sol, self.nodes[i]) for i, e in enumerate(self.fun_constraints) ]))
        while sol != f:
            for i, e in enumerate(self.fun_constraints):
                sol[e] = self.fun_constraints[e](sol, e)
            f = dict(zip(self.nodes, [ self.fun_constraints[e](sol, self.nodes[i]) for i, e in enumerate(self.fun_constraints) ]))

        return sol
