import heapq
import math
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        flipped = [-x for x in nums]
        heapq.heapify(flipped)

        ans = 0
        for _ in range(k):
            num = heapq.heappop(flipped)
            ans -= num
            num = math.ceil(num / 3)
            heapq.heappush(flipped, num)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MaximalScoreAfterApplyingKOperations(Solution):
    pass
