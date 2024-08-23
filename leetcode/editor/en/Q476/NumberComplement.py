# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def findComplement(self, num: int) -> int:
        x = 0
        stop = len(bin(num)[2::])
        for i in range(stop):
            x |= (0 if ((1 << i) & num) != 0 else 1) << i
        return x


# leetcode submit region end(Prohibit modification and deletion)


class NumberComplement(Solution):
    pass
