from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generatePossibleNextMoves(self, currentState):
        """
        :type currentState: str
        :rtype: List[str]
        """
        N = len(currentState)
        ans = []
        for i in range(0, N - 1):
            if currentState[i:i + 2] == '++':
                ans.append(currentState[:i] + '--' + currentState[i + 2::])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class FlipGame(Solution):
    pass
