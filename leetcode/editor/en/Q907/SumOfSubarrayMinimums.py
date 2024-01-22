from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:


        N = len(arr)
        def previousLessElement(nums):
            PLE = [-1] * len(nums)
            stack = []
            for i in range(len(nums)-1,-1,-1):
                while len(stack) > 0 and nums[i] < nums[stack[-1]]:
                    PLE[stack.pop()] = i
                stack.append(i)
            return PLE
        def nextLessElement(nums):
            NLE = [N] * N
            stack = []
            for i in range(len(nums)):
                while len(stack) > 0 and nums[i] <= nums[stack[-1]]:
                    NLE[stack.pop()] = i
                stack.append(i)
            return NLE

        PLE = previousLessElement(arr)
        NLE = nextLessElement(arr)
        ans = 0
        MOD = 10 ** 9 + 7
        for i in range(N):
            reach = NLE[i] - i
            reach_behind = i - PLE[i]
            degree = reach_behind * reach
            ans += ((arr[i] * degree) % MOD)

        ans %= MOD
        return ans

        
# leetcode submit region end(Prohibit modification and deletion)


class SumOfSubarrayMinimums(Solution):
    pass