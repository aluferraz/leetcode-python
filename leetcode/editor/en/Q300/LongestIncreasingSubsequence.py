from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        lis = [-1] * (N + 1)
        lis[0] = 0

        def good(idx, cur):
            return nums[lis[idx]] < nums[cur]
        longest = 1

        for i in range(N):

            left = 0
            right = longest
            while left < right:
                mid = (left + right) // 2
                if good(mid, i):
                    left = mid + 1
                else:
                    right = mid

            if lis[left] != -1:
                if nums[i] < nums[lis[left]]:
                    lis[left] = i
            else:
                lis[left] = i
            longest = max(left + 1, longest)
        return longest



# leetcode submit region end(Prohibit modification and deletion)


class LongestIncreasingSubsequence(Solution):
    pass
