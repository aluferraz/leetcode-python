import math

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        N = len(img)
        M = len(img[0])

        def isValidIdx(y, x):
            return y >= 0 and y < N and x >= 0 and x < M

        ans = [[0 for _ in range(M)] for _ in range(N)]

        for i in range(N):
            for j in range(M):
                cnt = 1
                tot = img[i][j]
                if isValidIdx(i - 1, j - 1):
                    tot += img[i - 1][j - 1]
                    cnt += 1
                if isValidIdx(i - 1, j + 1):
                    tot += img[i - 1][j + 1]
                    cnt += 1
                if isValidIdx(i + 1, j - 1):
                    tot += img[i + 1][j - 1]
                    cnt += 1
                if isValidIdx(i + 1, j + 1):
                    tot += img[i + 1][j + 1]
                    cnt += 1
                if isValidIdx(i - 1, j):
                    tot += img[i - 1][j]
                    cnt += 1
                if isValidIdx(i + 1, j):
                    tot += img[i + 1][j]
                    cnt += 1
                if isValidIdx(i, j - 1):
                    tot += img[i][j - 1]
                    cnt += 1
                if isValidIdx(i, j + 1):
                    tot += img[i][j + 1]
                    cnt += 1
                ans[i][j] = tot // cnt
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class ImageSmoother(Solution):
    pass
