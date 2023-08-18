import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        queue = collections.deque()
        N = len(mat)
        M = len(mat[0])
        INF = 10 ** 20

        ans = [[INF for _ in range(M)] for _ in range(N)]

        DIRECTIONS = [
            (1, 0),
            (-1, 0),
            (0, -1),
            (0, 1)
        ]

        def isValidIdx(i, j):
            return i >= 0 and i < N and j >= 0 and j < M

        for i in range(N):
            for j in range(M):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    for (y, x) in DIRECTIONS:
                        neighboorI = i + y
                        neighboorJ = j + x
                        if isValidIdx(neighboorI, neighboorJ):
                            if mat[neighboorI][neighboorJ] == 1:
                                ans[neighboorI][neighboorJ] = 1
        for i in range(N):
            for j in range(M):
                if ans[i][j] == 1:
                    queue.append((i, j))

        while len(queue) > 0:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                dist = ans[i][j]

                for (y, x) in DIRECTIONS:
                    if isValidIdx(i + y, j + x):
                        neighboorI = i + y
                        neighboorJ = j + x
                        if mat[neighboorI][neighboorJ] == 1 and ans[neighboorI][neighboorJ] > dist + 1:
                            queue.append((neighboorI, neighboorJ))
                            ans[neighboorI][neighboorJ] = min(ans[neighboorI][neighboorJ], dist + 1)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class Zero1Matrix(Solution):
    pass
