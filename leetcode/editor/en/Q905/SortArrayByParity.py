from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odds = []
        even = []
        N = len(nums)
        for i in range(N):
            if nums[i] % 2 == 1:
                odds.append(nums[i])
            else:
                even.append(nums[i])
        return even + odds


# leetcode submit region end(Prohibit modification and deletion)


class SortArrayByParity(Solution):
    pass
