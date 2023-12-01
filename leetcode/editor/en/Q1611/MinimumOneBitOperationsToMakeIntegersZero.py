import sys

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}

        def get_cost(bin_n, start, must_be):
            N = len(bin_n)
            initial_number = "".join(bin_n[start::])
            if (initial_number, must_be) in cache:
                cost, final_number = cache[(initial_number, must_be)]
                fpos = 0
                for i in range(start, N):
                    bin_n[i] = final_number[fpos]
                    fpos += 1
                return cost

            if start == N - 1:
                if bin_n[start] == must_be:
                    return 0
                bin_n[start] = must_be
                return 1
            cost = 0
            # for i in range(start, N):
            if bin_n[start] != must_be:
                cost = 1 + get_cost(bin_n, start + 1, '1')
            bin_n[start] = must_be
            cost += get_cost(bin_n, start + 1, '0')

            final_number = "".join(bin_n[start::])
            cache[(initial_number, must_be)] = (cost, final_number)

            return cost

        number = [x for x in bin(n)[2::]]
        ans = get_cost(number, 0, '0')
        return ans

    # leetcode submit region end(Prohibit modification and deletion)


class MinimumOneBitOperationsToMakeIntegersZero(Solution):
    pass
