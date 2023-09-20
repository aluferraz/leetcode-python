import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        weakest = []
        N = len(mat)
        for i in range(N):
            weakest.append((sum(mat[i]), i))
        heapq.heapify(weakest)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(weakest)[1])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class TheKWeakestRowsInAMatrix(Solution):
    pass
