from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = [0 for _ in range(max(nums)+1)]

        for n in nums:
            arr[n] += 1

        ans = -1

        for m in range(len(arr)):
            if arr[m] == 1:
                ans = m

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class LargestUniqueNumber(Solution):
    pass
