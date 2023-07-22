from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxDivScore(self, nums, divisors):
        """
        :type nums: List[int]
        :type divisors: List[int]
        :rtype: int
        """
        max_score = 0
        divisors.sort()
        ans = divisors[0]

        for d in divisors:
            score = 0
            for n in nums:
                if n % d == 0:
                    score += 1
            if score > max_score:
                max_score = score
                ans = d
        return ans

        # leetcode submit region end(Prohibit modification and deletion)


class FindTheMaximumDivisibilityScore(Solution):
    pass
