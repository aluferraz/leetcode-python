from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numberOfBeautifulIntegers(self, low, high, k):
        """
        :type low: int
        :type high: int
        :type k: int
        :rtype: int
        """
        cache = {}

        def beautiful_nums(remainder, pos, original, threshold, started, even, odd):

            if pos == len(original):
                if even == odd and remainder % k == 0 and started:
                    return 1
                return 0
            if (remainder, pos, original, threshold, started, even, odd) in cache:
                return cache[(remainder, pos, original, threshold, started, even, odd)]
            ans = 0
            if not started:
                ans = beautiful_nums(0,
                                     pos + 1,
                                     original,
                                     False,
                                     False,
                                     0,
                                     0)

            # 7 % k
            # 74 % k
            # ( 7 * 10 + 4 ) % k
            # ( 7 % k * 10 % k + 4 % k ) % k

            if threshold:
                limit = int(original[pos])
            else:
                limit = 9

            for i in range(limit + 1):
                started = started or i > 0
                new_remainder = ((remainder * 10) + i) % k
                new_even = even
                new_odd = odd
                if started:
                    if i % 2 == 0:
                        new_even += 1
                    else:
                        new_odd += 1
                    ans += beautiful_nums(new_remainder,
                                          pos + 1,
                                          original,
                                          threshold and i == limit,
                                          started,
                                          new_even,
                                          new_odd)
            cache[(remainder, pos, original, threshold, started, even, odd)] = ans
            return ans

        high_nums = beautiful_nums(0, 0, str(high), True, False, 0, 0)
        low_nums = beautiful_nums(0, 0, str(low), True, False, 0, 0)
        return high_nums - low_nums

        # leetcode submit region end(Prohibit modification and deletion)


class NumberOfBeautifulIntegersInTheRange(Solution):
    pass
