# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0
        for i in range(32):
            if ((1 << i) & start) != ((1 << i) & goal):
                ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MinimumBitFlipsToConvertNumber(Solution):
    pass
