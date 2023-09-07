from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        N = len(nums)

        def bin_search(target, left):
            right = N
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left

        def bin_search_last(target, left):
            right = N
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return left

        ans = 0
        for i in range(N):
            complement = lower - nums[i]
            boundary = upper - nums[i]
            start = bin_search(complement, i + 1)
            end = bin_search_last(boundary, i + 1)
            if start > i and end > i:
                ans += end - start
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class CountTheNumberOfFairPairs(Solution):
    pass
