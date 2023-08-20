from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """

        edges.sort(key=lambda x: x[2])
        parents = [-1] * n
        INF = 10 ** 20
        cost_unit = [INF] * n

        def union(i, j, w):
            parentI = find(i)
            parentJ = find(j)
            if parentI == parentJ:
                return
            if parents[parentJ] < parents[parentI]:
                return union(j, i, w)
            parents[parentI] += parents[parentJ]
            cost_unit[j] = w
            parents[parentJ] = parentI

        def find(i):
            while parents[i] >= 0:
                i = parents[i]
            return i

        critical = []
        pseudo_critical = []

        for (u, v, w) in edges:
            parentU = find(u)
            parentV = find(v)

            if parentU != parentV:
                critical.append(u)
                critical.append(v)
                union(u, v, w)
            else:
                if w == cost_unit[u] or w == cost_unit[v]:
                    pseudo_critical.append(u)
                    pseudo_critical.append(v)

        return [critical, pseudo_critical]


# leetcode submit region end(Prohibit modification and deletion)


class FindCriticalAndPseudoCriticalEdgesInMinimumSpanningTree(Solution):
    pass
