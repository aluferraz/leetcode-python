from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        ans = [0] * n
        ans[0] = 1

        for i in range(1, n):
            if i < 7:
                ans[i] = ans[i - 1] + 1
            else:
                ans[i] = ans[i - 7] + 1
        return sum(ans)


# leetcode submit region end(Prohibit modification and deletion)


class CalculateMoneyInLeetcodeBank(Solution):
    pass
