# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        coordinates.sort()
        slopes = set()
        prevY, prevX = coordinates[0]
        N = len(coordinates)
        for i in range(1, N):
            y, x = coordinates[i]
            rise = (y - prevY)
            run = (x - prevX)
            if rise == 0:
                slopes.add((float('inf'), float('inf')))
            elif run == 0:
                slopes.add((0, 0))
            else:
                divisor = math.gcd(rise, run)
                slopes.add((rise / divisor, run / divisor))
            prevY, prevX = y, x

        return len(slopes) == 1


# leetcode submit region end(Prohibit modification and deletion)


class CheckIfItIsAStraightLine(Solution):
    pass
