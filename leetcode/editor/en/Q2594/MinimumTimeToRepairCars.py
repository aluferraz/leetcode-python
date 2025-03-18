import math
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort()
        N = len(ranks)

        def good(max_time):
            cars_repaired = 0
            for i in range(N):
                can_repair = math.floor(math.sqrt(max_time / ranks[i]))
                cars_repaired += can_repair
            return cars_repaired >= cars

        left = 0
        right = ranks[-1] * (cars ** 2)
        while left < right:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid + 1
        return left


# leetcode submit region end(Prohibit modification and deletion)


class MinimumTimeToRepairCars(Solution):
    pass
