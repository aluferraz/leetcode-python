from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        N = len(s)
        zeros = [0] * N
        zeros[0] = 1 if s[0] == "0" else 0
        for i in range(1, N):
            zeros[i] = zeros[i - 1] + (1 if s[i] == "0" else 0)

        ones = 0
        for i in range(N - 1):
            if s[i] == "1":
                ones += 1
            ones_right = (N - zeros[-1] - ones)
            ans_here = zeros[i] + ones_right
            ans = max(ans_here, ans)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MaximumScoreAfterSplittingAString(Solution):
    pass
