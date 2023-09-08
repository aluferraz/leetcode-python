from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        wsum = 0
        N = len(calories)
        ans = 0
        for i in range(N):
            wsum += calories[i]
            if i - k + 1 < 0:
                continue
            if i - k >= 0:
                wsum -= calories[i - k]
            if wsum < lower:
                ans -= 1
            if wsum > upper:
                ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class DietPlanPerformance(Solution):
    pass
