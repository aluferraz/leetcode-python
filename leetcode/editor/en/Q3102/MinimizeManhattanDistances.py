import collections
from functools import cache
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        N = len(points)
        # manhatan = abs(xi - xj) + abs(yi - yj)
        # manhatan = max ((xi - xj), (xj - xi)) + max ((yi - yj), (yj - yi))
        # manhatan = max (
        #  (xi + xj) + (yi + yj),
        #  (xi - xj) + (yi - yj),
        #  (xj + xi) + (yj + yi)
        #  (xj - xi) + (yi - yj)
        # )
        #now we can group the points
        # manhatan = max (
        #  (xi + yi) + (xj + yj),
        #  (xi - yi) + (xj - yj),
        #  (xj + yj) + (xi + yi)
        #  (xj - yi) + (xi - yj)
        # )

        points_sum = [
            (x[0] + x[1]) for x in points
        ].sort()
        points_sub = [
            (x[0] + x[1]) for x in points
        ].sort()

        #continue...

        ans = max(

        )

# leetcode submit region end(Prohibit modification and deletion)


class MinimizeManhattanDistances(Solution):
    pass