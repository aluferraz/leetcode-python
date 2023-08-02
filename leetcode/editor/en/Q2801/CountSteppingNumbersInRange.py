from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countSteppingNumbers(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """

        MOD = (10 ** 9) + 7

        # If !has_began we only have zeros

        def digit_dp(i, has_began, prev, threshold, original):
            if i == len(original):
                return 0
            ans = 0
            digit_dp(i + 1, has_began, )


        ans = 0
        return ans % MOD


# leetcode submit region end(Prohibit modification and deletion)


class CountSteppingNumbersInRange(Solution):
    pass
