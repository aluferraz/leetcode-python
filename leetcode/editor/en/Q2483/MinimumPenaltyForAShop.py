from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        N = len(customers)
        INF = 10 ** 20
        y_sum = [0] * N
        n_sum = [0] * N
        if customers[-1] == 'Y':
            y_sum[-1] = 1
        if customers[0] == 'N':
            n_sum[0] = 1
        for i in range(1, N):
            n_sum[i] = n_sum[i - 1]
            if customers[i] == 'N':
                n_sum[i] += 1
        for i in range(N - 2, -1, -1):
            y_sum[i] = y_sum[i + 1]
            if customers[i] == 'Y':
                y_sum[i] += 1
        best = (n_sum[-1])
        best_idx = N
        for i in range(N - 1, -1, -1):
            close_here = y_sum[i]
            open_until_here = n_sum[i - 1] if i - 1 > 0 else 0
            penalty = open_until_here + close_here
            if penalty <= best:
                best = penalty
                best_idx = i

        return best_idx


# leetcode submit region end(Prohibit modification and deletion)


class MinimumPenaltyForAShop(Solution):
    pass
