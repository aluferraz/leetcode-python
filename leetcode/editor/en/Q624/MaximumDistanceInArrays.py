from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        N = len(arrays)
        INF = 10 ** 20
        ans = -INF
        arrays.sort(key=lambda x: (x[0], x[-1]))
        max_seen = arrays[0][-1]
        for i in range(1, N):
            ans = max(ans, abs(max_seen - arrays[i][0]))
            ans = max(ans, abs(arrays[0][0] - arrays[i][-1]))
            max_seen = max(max_seen, arrays[i][-1])

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MaximumDistanceInArrays(Solution):
    pass
