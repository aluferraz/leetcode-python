from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        max_bef = [0] * N
        max_aft = [0] * N
        max_bef[0] = height[0]
        max_aft[-1] = height[-1]
        for i in range(1, N):
            max_bef[i] = max(max_bef[i-1], height[i])
        for i in range(N-2,-1,-1):
            max_aft[i] = max(max_aft[i+1], height[i])
        ans = [0] * N

        for i in range(1, N-1):
            trapped = min(max_bef[i-1], max_aft[i+1]) - height[i]
            ans[i] = max(trapped,0)
        return sum(ans)

# leetcode submit region end(Prohibit modification and deletion)


class TrappingRainWater(Solution):
    pass