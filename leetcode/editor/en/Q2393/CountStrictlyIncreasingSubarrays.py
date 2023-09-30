from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.append(-1)
        N = len(nums)

        size = 1
        ans = 0
        for i in range(1, N):
            if nums[i] > nums[i - 1]:
                size += 1
            else:
                ans += (size * (size + 1)) // 2
                size = 1

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class CountStrictlyIncreasingSubarrays(Solution):
    pass
