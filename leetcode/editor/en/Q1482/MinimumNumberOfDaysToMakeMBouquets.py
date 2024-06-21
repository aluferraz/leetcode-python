from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        N = len(bloomDay)
        if (m * k) > N:
            return -1

        def good(target):
            count = 0
            current = 0
            for i in range(N):
                if bloomDay[i] > target:
                    current = 0
                else:
                    current += 1
                if current == k:
                    count += 1
                    current = 0
            return count >= m

        left = 1
        right = max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid + 1
        return left


# leetcode submit region end(Prohibit modification and deletion)


class MinimumNumberOfDaysToMakeMBouquets(Solution):
    pass
