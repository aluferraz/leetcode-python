import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def validSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def next_lesser_element(arr):
            N = len(arr)
            NLE = [N] * N
            stack = collections.deque()
            for i in range(N):
                while len(stack) > 0 and arr[i] < arr[stack[-1]]:
                    NLE[stack.pop()] = i
                stack.append(i)
            return NLE

        NLE = next_lesser_element(nums)
        N = len(nums)
        ans = 0
        for i in range(N):
            can_reach = NLE[i]
            degree_of_freedom = (can_reach - i - 1)
            ans += (1 + (1 * degree_of_freedom))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfValidSubarrays(Solution):
    pass
