from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def colorTheArray(self, N, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # unfinished
        ans = [0] * len(queries)
        arr = [-i for i in range(1, N + 1)]
        cans = 0
        for j in range(len(queries)):
            (i, c) = queries[j]
            ans[j] = cans
            if arr[i] == c:
                continue

            if i > 0:
                if arr[i - 1] == arr[i]:
                    cans -= 1

                if arr[i - 1] == c:
                    cans += 1
            if i + 1 < N:
                if arr[i + 1] == arr[i]:
                    cans -= 1
                if arr[i + 1] == c:
                    cans += 1
            arr[i] = c
            ans[j] = cans
        return ans

        # leetcode submit region end(Prohibit modification and deletion)


class NumberOfAdjacentElementsWithTheSameColor(Solution):
    pass
