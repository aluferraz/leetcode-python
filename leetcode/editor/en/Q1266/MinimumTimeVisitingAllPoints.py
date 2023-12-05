from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        N = len(points)

        def go(i, j, k):
            if k == N:
                return 0
            if [i, j] == points[k]:
                return go(i, j, k + 1)
            target = points[k]
            vmove = target[0] - i
            hmove = target[1] - j
            if vmove < 0:
                vmove = -1
            if vmove > 0:
                vmove = 1
            if hmove < 0:
                hmove = -1
            if hmove > 0:
                hmove = 1
            return 1 + go(i + vmove, j + hmove, k)

        return go(points[0][0], points[0][1], 1)


# leetcode submit region end(Prohibit modification and deletion)


class MinimumTimeVisitingAllPoints(Solution):
    pass
