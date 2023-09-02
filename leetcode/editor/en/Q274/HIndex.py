from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()

        def good(hidx):
            left = 0
            right = len(citations) - 1
            ans = len(citations)
            while left <= right:
                mid = (left + right) // 2
                if citations[mid] >= hidx:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1


            return (len(citations) - ans) >= hidx

        left = 0
        right = len(citations)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if good(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class HIndex(Solution):
    pass
