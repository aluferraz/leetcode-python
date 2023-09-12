import collections
from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """

        MOD = (10 ** 9) + 7

        if n == 1:
            return 1
        count = 1
        for i in range(2, n - 1):
            dividers = (i - 1) * 2
            choices = dividers + 1
            count = (choices * (choices + 1)) // 2 * count
            count %= MOD
        return count % MOD


# leetcode submit region end(Prohibit modification and deletion)


class CountAllValidPickupAndDeliveryOptions(Solution):
    pass
