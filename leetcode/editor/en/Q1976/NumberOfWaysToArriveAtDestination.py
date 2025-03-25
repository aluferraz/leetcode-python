import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        ans = 0
        INF = 10 ** 20
        min_time = INF
        q = collections.deque()
        adj_list = collections.defaultdict(dict)
        for f, t, w in roads:
            if t not in adj_list[f]:
                adj_list[f][t] = INF
            adj_list[f][t] = min(w, adj_list[f][t])
            t, f = f, t
            if t not in adj_list[f]:
                adj_list[f][t] = INF
            adj_list[f][t] = min(w, adj_list[f][t])
        q.append((0, 0))
        visited = {}

        while q:
            size = len(q)
            for _ in range(size):
                node, cost = q.popleft()
                if node == n - 1:
                    if cost > min_time:
                        continue
                    if cost < min_time:
                        min_time = cost
                        ans = 0
                    ans += 1
                for t, w in adj_list[node].items():
                    new_cost = cost + w
                    if new_cost > min_time:
                        continue
                    if t in visited:
                        if new_cost <= visited[t]:
                            q.append((t, new_cost))
                    else:
                        q.append((t, new_cost))
                        visited[t] = new_cost
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfWaysToArriveAtDestination(Solution):
    pass
