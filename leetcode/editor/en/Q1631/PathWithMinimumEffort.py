import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """

        N = len(heights)
        M = len(heights[0])
        INF = 10 ** 20
        DIRECTIONS = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        def good(threshold):
            q = collections.deque()
            q.append((0, 0, 0))
            ans = INF
            visited = [[None for _ in range(M)] for _ in range(N)]
            visited[0][0] = 0

            while len(q) > 0:
                size = len(q)
                for _ in range(size):
                    i, j, diff = q.popleft()
                    if (i, j) == (N - 1, M - 1):
                        ans = min(diff, ans)
                    for (y, x) in DIRECTIONS:
                        newY = i + y
                        newX = j + x

                        if newY >= 0 and newY < N and newX >= 0 and newX < M:
                            new_diff = max(diff, abs(heights[i][j] - heights[newY][newX]))
                            if new_diff > threshold:
                                continue
                            if visited[newY][newX] is None:
                                visited[newY][newX] = new_diff
                                if (newY, newX) != (N - 1, M - 1):
                                    q.append((newY, newX, new_diff))
                                else:
                                    ans = min(new_diff, ans)
                            elif new_diff < visited[newY][newX]:
                                visited[newY][newX] = new_diff
                                if (newY, newX) != (N - 1, M - 1):
                                    q.append((newY, newX, new_diff))
                                else:
                                    ans = min(new_diff, ans)
            return ans <= threshold

        # return good(0)
        left = 0
        right = 10 ** 6 + 1

        while left < right:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid + 1
        return left


# leetcode submit region end(Prohibit modification and deletion)


class PathWithMinimumEffort(Solution):
    pass
