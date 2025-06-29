from cfg import *
from math import inf
"""
based on 
(fast algorithm for findign dominators)
https://www.cs.utexas.edu/~misra/Lengauer+Tarjan.pdf
https://www.cs.princeton.edu/courses/archive/fall03/cs528/handouts/a%20fast%20algorithm%20for%20finding.pdf

(algorithm for finding dominance frontiers)
https://www.cs.utexas.edu/~pingali/CS380C/2010/papers/ssaCytron.pdf
"""

class DominatorsTree():
    def __init__(self, cfg):
        self.order = dict()
        self.tree = dict()
        self.cfg_dfs_order(cfg.start_stm)
        self.root = dict(zip([x for x in self.order], [x for x in self.order]))
        self.sd = dict()
        self.idoms = self.dominators()


    def cfg_dfs_order(self, node, i=0, parent=None):
        if node not in self.order:
            self.tree[node] = parent
            self.order[node] = i
            i+=1
        else:
            return i

        for s in node.successors:
            i = self.cfg_dfs_order(s, i, node)
        return i


    def compute_semidom(self, node):
        sd1 = inf
        sd2 = inf
        for p in node.predecessors:
            if self.order[p] < self.order[node]:
                sd1 = min(sd1, self.order[p])
            else:
                sd2 = min(sd2, self.compute_sd2(node, p))
        self.sd[node] = min(sd1, sd2)
        self.root[node] = self.sd[node]


    def vertex(self, i):
        for v, n in self.order.items():
            if n==i:
                return v
        raise ValueError(f"Given node number does not exis: {i}")


    def compute_sd2(self, r, n):
        if self.order[r] < self.order[n]:
            return self.compute_sd2(r, self.vertex(self.root[n]))
        else:
            return self.order[n]


    def min_internal(self, sd_num, w):
        min_sd = inf
        potential_internals = [w]
        u = self.tree[w]
        while self.order[u] != sd_num:
            if min_sd > self.sd[u]:
                min_sd = self.sd[u]
                potential_internals = [self.vertex(min_sd)]
            else:
                potential_internals.append(u)
            u = self.tree[u]
        return potential_internals[0]


    def dominators(self):
        buckets = dict(zip([x for x in range(len(self.order))], [set() for x in range(len(self.order))])) 
        internals = dict()
        for w in sorted(self.order, key=self.order.get, reverse=True):
            if self.order[w] != 0:
                self.compute_semidom(w)
                buckets[self.sd[w]] |= {w}

        for k in range(len(self.order)):
            for w in buckets[k]:
                min_sd = inf
                internals[w] = self.min_internal(k, w)

        idoms = dict()
        for i in range(1, len(self.order)):
            w = self.vertex(i)
            if self.order[w] == self.order[internals[w]]:
                idoms[w] = self.sd[w]
            else:
                idoms[w] = self.order[internals[w]]
        return idoms

    
class DominanceFrontier(DominatorsTree):
    def __init__(self, cfg):
        super(DominanceFrontier, self).__init__(cfg)
        self.dom_tree = self.dominance_tree()
        self.dom_frontier = dict()

        for x in sorted(self.order, key=self.order.get, reverse=True):
            self.dom_frontier[x] = set()
            for y in x.successors:
                if self.vertex(self.idoms[y]) != x:
                    self.dom_frontier[x] |= {y}
            for z in self.dom_tree[x]:
                for y in self.dom_frontier[z]:
                    if self.vertex(self.idoms[y]) != x:
                        self.dom_frontier[x] |= {y}


    def dominance_tree(self):
        dom_tree = dict(zip([x for x in self.order], [set() for x in self.order]))
        for node in self.tree:
            if self.tree[node] is not None:
                dom_tree[self.tree[node]] |= {node}
        return dom_tree
