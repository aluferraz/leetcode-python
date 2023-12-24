from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        vert = 0
        hori = 0

        hist = set()
        hist.add((vert, hori))

        for c in path:
            if c == 'N':
                vert += 1
            elif c == 'S':
                vert -= 1
            elif c == 'W':
                hori += 1
            elif c == 'E':
                hori -= 1
            if (vert, hori) in hist:
                return True
            hist.add((vert, hori))
        return False


# leetcode submit region end(Prohibit modification and deletion)


class PathCrossing(Solution):
    pass
