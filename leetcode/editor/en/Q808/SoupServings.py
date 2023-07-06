from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def soupServings(self, N):
        """
        :type n: int
        :rtype: float
        """
        scenarios = [
            (100, 0),
            (75, 25),
            (50, 50),
            (25, 75),
        ]

        cache = {}

        def countSoups(aSoup, bSoup):
            if (aSoup, bSoup) in cache:
                return cache[aSoup, bSoup]
            if aSoup == 0 or bSoup == 0:
                if aSoup == 0 and bSoup > 0:
                    return 1
                if aSoup == 0 and bSoup == 0:
                    return 0.5
                else:
                    return 0
            prob = 0
            for a, b in scenarios:
                prob += (0.25 * countSoups(
                    max(aSoup - a, 0),
                    max(bSoup - b, 0)
                ))
            cache[(aSoup, bSoup)] = prob
            return prob

        prob = countSoups(N, N)
        return prob

    # leetcode submit region end(Prohibit modification and deletion)


class SoupServings(Solution):
    pass
