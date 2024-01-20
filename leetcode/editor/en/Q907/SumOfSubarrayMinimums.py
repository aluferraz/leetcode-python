from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        ans = arr[0]
        N = len(arr)
        min_seen = arr[0]
        for i in range(1,N):
            ans += arr[i]
            min_seen = min(min_seen, arr[i])
            ans += min_seen
        return ans

        
# leetcode submit region end(Prohibit modification and deletion)


class SumOfSubarrayMinimums(Solution):
    pass