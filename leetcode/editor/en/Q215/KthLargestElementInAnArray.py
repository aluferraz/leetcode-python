import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nheap = [-n for n in nums]
        heapq.heapify(nheap)
        ans = -1
        for i in range(k):
            ans = -heapq.heappop(nheap)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class KthLargestElementInAnArray(Solution):
    pass
