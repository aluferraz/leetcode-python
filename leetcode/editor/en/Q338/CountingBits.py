from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n + 1)

        for i in range(len(ans)):
            ans[i] = i.bit_count()
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class CountingBits(Solution):
    pass
