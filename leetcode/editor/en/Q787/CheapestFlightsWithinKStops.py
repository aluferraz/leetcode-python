import collections
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0
        q = collections.deque()
        seen = {}
        adj_list = collections.defaultdict(list)
        for f,t,p in flights:
            adj_list[f].append((t,p))

        q.append((src, 0, 0))
        ans = 10 ** 20

        while len(q) > 0:
            size = len(q)
            for _ in range(size):
                air, jumps, cost = q.popleft()
                if air == dst:
                    ans = min(ans, cost)
                if jumps == k+1:
                    break
                seen[air] = cost
                for next_air, price in adj_list[air]:
                    if next_air not in seen or \
                            (cost + price) <= seen[next_air]:
                        q.append((next_air, jumps+1, cost+price))
        return ans
# leetcode submit region end(Prohibit modification and deletion)


class CheapestFlightsWithinKStops(Solution):
    pass