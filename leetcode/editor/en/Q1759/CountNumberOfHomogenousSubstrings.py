from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        def natural_sum(k):
            if k == 0:
                return 0
            return (k * (k + 1)) // 2

        N = len(s)
        ans = 0
        last_break = 0
        for i in range(1, N):
            if s[i] == s[i - 1]:
                continue
            equal = i - last_break
            ans = ((ans % MOD) + (natural_sum(equal) % MOD)) % MOD
            last_break = i
        equal = N - last_break
        ans = ((ans % MOD) + (natural_sum(equal) % MOD)) % MOD
        return ans % MOD

    # leetcode submit region end(Prohibit modification and deletion)


class CountNumberOfHomogenousSubstrings(Solution):
    pass
