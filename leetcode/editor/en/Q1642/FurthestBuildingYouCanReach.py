import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        N = len(heights)

        min_bricks_until = [0] * N
        maxes = []
        max_discount = 0
        for i in range(1, N):
            diff = max(heights[i] - heights[i - 1], 0)
            if diff > 0:
                heapq.heappush(maxes, diff)
                max_discount += diff
                if len(maxes) > ladders:
                    max_discount -= heapq.heappop(maxes)
            min_bricks_until[i] = (min_bricks_until[i - 1] + diff)
            if min_bricks_until[i] - max_discount > bricks:
                return max(i - 1, 0)

        return N - 1


# leetcode submit region end(Prohibit modification and deletion)


class FurthestBuildingYouCanReach(Solution):
    pass
