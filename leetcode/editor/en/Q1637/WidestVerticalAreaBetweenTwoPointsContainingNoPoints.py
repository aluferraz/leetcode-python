from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()

        ans = 0
        prev = points[0][0]

        for x, _ in points:
            ans = max((prev - x), ans)
            prev = x
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class WidestVerticalAreaBetweenTwoPointsContainingNoPoints(Solution):
    pass
