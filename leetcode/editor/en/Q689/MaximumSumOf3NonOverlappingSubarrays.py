import collections
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)

        # 1) Compute prefix sums for fast range-sum queries
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # sum_sub[i] = sum of subarray of length k starting at index i
        # (i.e., nums[i] + nums[i+1] + ... + nums[i+k-1])
        sum_sub = [0] * (n - k + 1)
        for i in range(n - k + 1):
            sum_sub[i] = prefix[i + k] - prefix[i]

        # 2) left[i] = the index of the maximum subarray (of length k)
        #    in sum_sub among indices [0..i]
        left = [0] * (n - k + 1)
        best_idx = 0  # best index so far for the left subarray
        for i in range(n - k + 1):
            if sum_sub[i] > sum_sub[best_idx]:
                best_idx = i
            left[i] = best_idx

        # 3) right[i] = the index of the maximum subarray (of length k)
        #    in sum_sub among indices [i..(n-k)]
        right = [0] * (n - k + 1)
        best_idx = n - k  # best index so far for the right subarray
        for i in range(n - k, -1, -1):
            # If we find a strictly greater sum, or same sum but smaller index, update
            if sum_sub[i] >= sum_sub[best_idx]:
                best_idx = i
            right[i] = best_idx

        # 4) Now find the best "middle" index j to maximize sum_sub[left[j-k]] + sum_sub[j] + sum_sub[right[j+k]]
        ans = None
        max_sum = -float('inf')
        # Middle subarray can start from k to (n - 2k) inclusive
        for j in range(k, n - 2 * k + 1):
            i = left[j - k]  # best left index up to j-k
            l = right[j + k]  # best right index from j+k onwards
            current_sum = sum_sub[i] + sum_sub[j] + sum_sub[l]
            if current_sum > max_sum:
                max_sum = current_sum
                ans = [i, j, l]

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MaximumSumOf3NonOverlappingSubarrays(Solution):
    pass
    