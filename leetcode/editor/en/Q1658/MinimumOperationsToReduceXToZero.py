import sys

from functools import cache
from typing import List

sys.setrecursionlimit(10 ** 9)


# leetcode submit region begin(Prohibit modification and deletion)

class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        N = len(nums)
        INF = 10 ** 20
        psum = [0] * N
        ssum = [0] * N
        psum[0] = nums[0]
        ssum[0] = nums[-1]
        for i in range(1, N):
            psum[i] = psum[i - 1] + nums[i]
            ssum[i] = ssum[i - 1] + nums[N - i - 1]
        if (psum[0] > x and ssum[0] > x) or psum[-1] < x:
            return -1

        def bin_search(left, right, target, arr):
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        ans = INF
        for i in range(N):
            if psum[i] > x:
                break
            diff = x - psum[i]
            if diff == 0:
                ans = min(ans, (i + 1))
            else:
                complement = bin_search(0, N - (i + 2), diff, ssum)
                if complement != -1:
                    ans = min(ans, (i + 1 + complement + 1))
        for i in range(N):
            if ssum[i] > x:
                break
            diff = x - ssum[i]
            if diff == 0:
                ans = min(ans, i + 1)
            else:
                complement = bin_search(0, N - (i + 2), diff, psum)
                if complement != -1:
                    ans = min(ans, (i + 1 + complement + 1))
        if ans >= INF:
            return -1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MinimumOperationsToReduceXToZero(Solution):
    pass
