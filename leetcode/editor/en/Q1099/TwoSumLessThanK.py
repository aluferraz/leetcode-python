from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        N = len(nums)

        def find_closest(left, target):
            right = N - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans

        ans = -1
        for i in range(N):
            if nums[i] <= k:
                rest = k - nums[i]
                best_pair = find_closest(i + 1, rest)
                if best_pair != -1:
                    ans = max(ans, nums[i] + nums[best_pair])

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class TwoSumLessThanK(Solution):
    pass
