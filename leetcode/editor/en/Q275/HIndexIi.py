from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        left = 0
        right = N - 1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= N - mid:
                ans = N - mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class HIndexIi(Solution):
    pass
