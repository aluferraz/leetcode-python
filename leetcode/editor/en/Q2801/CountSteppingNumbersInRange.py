from functools import cache
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
        cache = {}

        def digit_dp(i, tight, prev, current, has_started, original):
            if i == len(original):
                return 1 if has_started else 0
            if (i, tight, prev, has_started, original) in cache:
                return cache[(i, tight, prev, has_started, original)]
            upper = 10
            if tight:
                upper = int(original[i])
            ans = 0
            for d in range(upper):
                if abs(d - prev) == 1 or not has_started:
                    current[i] = d
                    ans += digit_dp(i + 1, False, current[i], current, (d > 0 or has_started), original)
            if tight:
                if abs(upper - prev) == 1 or not has_started:
                    current[i] = upper
                    ans += digit_dp(i + 1, True, current[i], current, (upper > 0 or has_started), original)
            cache[(i, tight, prev, has_started, original)] = ans
            return ans

        def get_ans(arr):
            tight_upper = int(arr[0])
            ans = 0
            current = [0] * len(arr)

            for d in range(tight_upper):
                current[0] = d
                ans += digit_dp(1, False, d, current, d > 0, arr)
            current[0] = tight_upper
            ans += digit_dp(1, True, tight_upper, current, tight_upper > 0, arr)
            return ans

        ans = get_ans(high) - (get_ans(str(int(low) - 1)) if int(low) > 1 else 0)

        return ans % MOD


# leetcode submit region end(Prohibit modification and deletion)


class CountSteppingNumbersInRange(Solution):
    pass
