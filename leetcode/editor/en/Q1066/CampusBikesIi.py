from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        N = len(workers)
        M = len(bikes)
        INF = 10 ** 20
        cache = {}

        def go(i, mask):
            if i == N:
                return 0
            if (i, mask) in cache:
                return cache[(i, mask)]

            ans = INF

            for j in range(M):
                if mask & (1 << j) == 0:
                    ans = min(ans,
                              (abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1]))
                              +
                              go(i + 1, mask | (1 << j))

                              )
            cache[(i, mask)] = ans
            return ans

        return go(0, 0)


# leetcode submit region end(Prohibit modification and deletion)


class CampusBikesIi(Solution):
    pass
