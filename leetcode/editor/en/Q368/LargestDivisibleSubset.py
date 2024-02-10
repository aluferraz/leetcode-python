import heapq
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        ans = []
        N = len(nums)

        def go(cur, i):
            if i == N:
                if len(cur) > N:
                    nonlocal ans
                    ans = list(cur)
                return
            if len(cur) == 0 or nums[i] % cur[-1] == 0:
                heapq.heappush(cur, nums[i])
                go(cur, i + 1)
                heapq.heappop(cur)
            go(cur, i + 1)

        go([], 0)
        return ans

        
# leetcode submit region end(Prohibit modification and deletion)


class LargestDivisibleSubset(Solution):
    pass