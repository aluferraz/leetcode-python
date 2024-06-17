# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        seen = {0}
        for i in range(1, c + 1):
            square = i * i
            seen.add(square)
            if (c - square) in seen:
                return True
            if square > c:
                break
        return False


# leetcode submit region end(Prohibit modification and deletion)


class SumOfSquareNumbers(Solution):
    pass
