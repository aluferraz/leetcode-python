from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def colorTheArray(self, N, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        #unfinished
        ans = [0] * len(queries)
        arr = [-i for i in range(1, N + 1)]

        for j in range(len(queries)):
            (i, c) = queries[j]

        # leetcode submit region end(Prohibit modification and deletion)


class NumberOfAdjacentElementsWithTheSameColor(Solution):
    pass
