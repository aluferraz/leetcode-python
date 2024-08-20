# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_set = {1}
        ith_ugly = 1
        min_seen = 1
        for i in range(n):
            ith_ugly = min_seen
            ugly_set.discard(ith_ugly)
            ugly_set.add(ith_ugly * 2)
            ugly_set.add(ith_ugly * 3)
            ugly_set.add(ith_ugly * 5)
            min_seen = (ith_ugly * 2)
        return ith_ugly


# leetcode submit region end(Prohibit modification and deletion)


class UglyNumberIi(Solution):
    pass
