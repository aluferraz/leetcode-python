from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        N = len(quality)
        costs = list(zip(wage, quality))
        costs.sort(key=lambda x: (-x[0], x[1]))  # higher salary, lower quality
        print(costs)


# leetcode submit region end(Prohibit modification and deletion)


class MinimumCostToHireKWorkers(Solution):
    pass
