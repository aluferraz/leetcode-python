import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        def nextGreaterElement(arr):
            NGE = [len(arr)] * len(arr)
            stack = collections.deque()
            for i in range(0, len(arr)):
                while len(stack) > 0 and nums[i] > nums[stack[-1]]:
                    NGE[stack.pop()] = i
                stack.append(i)
            return NGE

        NGE = nextGreaterElement(nums)

        N = len(nums)

        def fill_arr(start_idx, mask):
            i = start_idx
            row = []
            while i < N:
                while mask & (1 << i) != 0:
                    i += 1
                if i >= N:
                    break
                mask |= (1 << i)
                row.append(nums[i])
                i = NGE[i]
            return row, mask

        mask = 0
        ans = []

        for i in range(N):
            if mask & (1 << i) == 0:
                row, used = fill_arr(i, mask)
                ans.append(row)
                mask |= used
        return ans

        # leetcode submit region end(Prohibit modification and deletion)


class ConvertAnArrayIntoA2dArrayWithConditions(Solution):
    pass
