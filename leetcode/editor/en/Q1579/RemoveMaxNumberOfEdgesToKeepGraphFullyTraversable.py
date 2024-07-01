import collections
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        N = n
        for i in range(len(edges)):
            t,u,v = edges[i]
            edges[i] = [t, u-1,v-1]
        parents_bob = [-1] * N
        parents_alice = [-1] * N

        def find(i,parents):
            path_comp = []
            while parents[i] >= 0:
                i = parents[i]
            while(len(path_comp) > 0):
                parents[path_comp.pop()] = i
            return i

        def union(u,v, parents):
            if u == v:
                return 1
            if parents[v] < parents[u]:
                return union(v,u, parents)
            parents[u] += parents[v]
            parents[v] = u
            return 0
        can_delete_both = 0
        for t, u, v in edges:
            if t == 3:
                can_delete_both += union(find(u, parents_alice), find(v, parents_alice),parents_alice)
                union(find(u, parents_bob), find(v, parents_bob),parents_bob)
        can_delete_alice = 0
        can_delete_bob = 0
        for t, u, v in edges:
            if t == 1:
                can_delete_alice += union(find(u, parents_alice), find(v, parents_alice),parents_alice)
            if t == 2:
                can_delete_bob += union(find(u, parents_bob), find(v, parents_bob),parents_bob)

        bob_root = 0
        alice_root = 0
        for i in range(N):
            if parents_alice[i] < 0:
                alice_root += 1
            if parents_bob[i] < 0:
                bob_root += 1

        if bob_root != 1 or alice_root != 1:
            return -1
        return can_delete_both + can_delete_alice + can_delete_bob









        
# leetcode submit region end(Prohibit modification and deletion)


class RemoveMaxNumberOfEdgesToKeepGraphFullyTraversable(Solution):
    pass
    