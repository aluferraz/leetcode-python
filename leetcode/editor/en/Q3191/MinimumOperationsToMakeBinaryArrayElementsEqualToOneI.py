from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        start = N
        for i in range(N):
            if nums[i] == 0:
                start = i
                break
        ops = 0
        for j in range(start, start + N):
            i = j % N
            if nums[i] == 0:
                ops += 1
                for k in range(i, i + 3):
                    nums[k % N] = (nums[k % N] + 1) % 2
        if nums.count(1) == N:
            return ops
        return -1


# leetcode submit region end(Prohibit modification and deletion)


class MinimumOperationsToMakeBinaryArrayElementsEqualToOneI(Solution):
    pass
