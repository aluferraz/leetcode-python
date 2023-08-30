from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def getMaxFunctionValue(self, receiver, k):
        """
        :type receiver: List[int]
        :type k: int
        :rtype: int
        """
        # binary lifting
        N = len(receiver)
        exp_max = 20
        dp = [[(0, 0) for _ in range(exp_max)] for _ in range(N)]

        for i in range(N):
            # 2**0  = 1
            dp[i][0] = (receiver[i], receiver[i])

        for l in range(1, exp_max):
            for i in range(N):
                pos, score = dp[dp[i][l - 1][0]][l - 1]
                dp[i][l] = (pos, score + dp[i][l - 1][1])

        best = 0

        for i in range(N):
            current = i
            ans_here = 0

            for l in range(exp_max):
                if k & (1 << l):
                    next_node, inc = dp[current][l]
                    ans_here += inc
                    current = next_node
            best = max(best, i + ans_here)

        return best

    # leetcode submit region end(Prohibit modification and deletion)


class MaximizeValueOfFunctionInABallPassingGame(Solution):
    pass
