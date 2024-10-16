# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumSteps(self, s: str) -> int:
        seenOne = False
        N = len(s)
        swaps = 0
        for i in range(N):
            if s[i] == '1':
                seenOne = True
            elif seenOne:
                swaps += 1
        return swaps


# leetcode submit region end(Prohibit modification and deletion)


class SeparateBlackAndWhiteBalls(Solution):
    pass
