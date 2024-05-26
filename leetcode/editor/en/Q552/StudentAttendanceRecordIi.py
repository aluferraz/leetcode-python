# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        cache = [[[-1 for _ in range(2)] for _ in range(3)] for _ in range(n)]

        def go(i, l, a):
            if l >= 3:
                return 0
            if a >= 2:
                return 0
            if i == n:
                return 1
            if cache[i][l][a] >= 0:
                return cache[i][l][a]
            ans = 0
            ans += (go(i + 1, 0, a) % MOD)  # Present
            ans += (go(i + 1, l + 1, a) % MOD)  # Late
            ans += (go(i + 1, 0, a + 1) % MOD)  # Absent
            cache[i][l][a] = ans
            return ans % MOD

        return go(0, 0, 0)


# leetcode submit region end(Prohibit modification and deletion)


class StudentAttendanceRecordIi(Solution):
    pass
