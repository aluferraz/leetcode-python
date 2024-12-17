import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    class Solution:
        def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
            graph = collections.defaultdict(list)
            for x in range(n - 1):
                graph[x].append(x + 1)

            def BFS():
                level, queue = 0, [0]
                seen = set()
                while queue:
                    next_level = []
                    for node in queue:
                        if node == n - 1:
                            return level
                        for child in graph[node]:
                            if child not in seen:
                                seen.add(child)
                                next_level.append(child)
                    queue = next_level
                    level += 1
                return level

            ans = []
            for orig, dest in queries:
                graph[orig].append(dest)
                ans.append(BFS())
            return ans


# leetcode submit region end(Prohibit modification and deletion)


class ShortestDistanceAfterRoadAdditionQueriesI(Solution):
    pass
