# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSteps(self, s: str) -> int:
        num = 0
        N = len(s)
        expo = 0
        for i in range(N - 1, -1, -1):
            if s[i] == "1":
                num += 2 ** expo
            expo += 1

        def go(number):
            if number == 1:
                return 0
            if number % 2 == 0:
                return 1 + go(number // 2)
            return 1 + go(number + 1)

        return go(num)


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfStepsToReduceANumberInBinaryRepresentationToOne(Solution):
    pass
