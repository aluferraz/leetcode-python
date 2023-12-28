from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        N = len(colors)
        rope = [0]
        ans = 0
        for i in range(1, N):
            if colors[i] == colors[rope[-1]]:
                if neededTime[i] <= neededTime[rope[-1]]:
                    ans += neededTime[i]
                    continue
                else:
                    ans += neededTime[rope.pop()]
            rope.append(i)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MinimumTimeToMakeRopeColorful(Solution):
    pass
