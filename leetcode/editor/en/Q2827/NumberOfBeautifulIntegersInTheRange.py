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

        def beautiful_nums(num, pos, original, threshold, started, even, odd):
            if pos == len(original):
                if even == odd and int("".join(num)) % k == 0:
                    return 1
                return 0


            # cache_key = ("".join(num))
            #
            # if cache_key in cache:
            #     return cache[cache_key]

            if threshold:
                limit = int(original[pos])
            else:
                limit = 9
            ans = 0
            for i in range(limit + 1):
                if not started and i > 0:
                    started = True
                num[pos] = str(i)

                ans += beautiful_nums(num,
                                      pos + 1,
                                      original,
                                      threshold and i == limit,
                                      started,
                                      even + (((i % 2) + 1) % 2) if started else even,
                                      odd + (i % 2))
            # cache[cache_key] = ans
            return ans

        num = ["0"] * len(str(high))
        high_arr = [int(n) for n in str(high)]
        low_arr = [int(n) for n in str(low - 1)]
        high_nums = beautiful_nums(num, 0, high_arr, True, False, 0, 0)
        cache = {}
        num = ["0"] * len(str(low - 1))
        low_nums = beautiful_nums(num, 0, low_arr, True, False, 0, 0)
        return high_nums - low_nums

        # leetcode submit region end(Prohibit modification and deletion)


class NumberOfBeautifulIntegersInTheRange(Solution):
    pass
