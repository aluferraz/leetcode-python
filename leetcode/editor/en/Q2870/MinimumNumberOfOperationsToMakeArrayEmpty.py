from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperations(self, nums: List[int]) -> int:

        nums.sort()
        INF = 10 ** 20
        N = len(nums)
        has_cache = [False] * N
        cache = [INF] * N

        def go(i):
            if i == N:
                return 0
            if i > N:
                return INF
            if has_cache[i]:
                return cache[i]
            ans = INF
            if i+1 < N and nums[i+1] == nums[i]:
                ans = min(ans, 1 + go(i+2))
                if i+2 < N and nums[i+2] == nums[i]:
                    ans = min(ans, 1 + go(i+3))
            cache[i] = ans
            has_cache[i] = True
            return ans
        ans = go(0)
        if ans >= INF:
            return -1
        return ans


        
# leetcode submit region end(Prohibit modification and deletion)


class MinimumNumberOfOperationsToMakeArrayEmpty(Solution):
    pass