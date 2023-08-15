from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        ans = 0
        jewels = set(jewels)
        for s in stones:
            if s in jewels:
                ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class JewelsAndStones(Solution):
    pass
