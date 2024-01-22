import heapq
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            a = heapq.heappop(sticks)
            b = heapq.heappop(sticks)
            cost += (a + b)
            heapq.heappush(sticks, (a + b))

        return cost


# leetcode submit region end(Prohibit modification and deletion)


class MinimumCostToConnectSticks(Solution):
    pass