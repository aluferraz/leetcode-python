import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(conditions):
            indegree = [0] * k
            prev = collections.defaultdict(list)
            for a, b in conditions:
                a -= 1
                b -= 1
                prev[a].append(b)
                indegree[b] += 1

            q = collections.deque()
            for i in range(k):
                if indegree[i] == 0:
                    q.append(i)
            ordering = []
            while len(q) > 0:
                now = q.popleft()
                ordering.append(now)
                for nxt in prev[now]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        q.append(nxt)

            return {x: i for i, x in enumerate(ordering)}

        rows = topological_sort(rowConditions)
        cols = topological_sort(colConditions)
        if len(rows) != k or len(cols) != k:
            return []
        ans = [[0 for _ in range(k)] for _ in range(k)]

        for i in range(k):
            ans[rows[i]][cols[i]] = i + 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class BuildAMatrixWithConditions(Solution):
    pass
