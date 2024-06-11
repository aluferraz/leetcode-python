from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        copyH = sorted(list(heights))
        N = len(heights)
        ans = 0
        for i in range(N):
            if copyH[i] != heights[i]:
                ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class HeightChecker(Solution):
    pass
