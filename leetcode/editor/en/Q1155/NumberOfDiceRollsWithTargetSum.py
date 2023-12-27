from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        cache = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        has_cache = [[False for _ in range(target + 1)] for _ in range(n + 1)]

        def go(i, target):
            if (target > i * k) or target <= 0:
                return 0
            if i == 1:
                if target > k:
                    return 0
                return 1
            if has_cache[i][target]:
                return cache[i][target]
            ans = 0
            for j in range(k, 0, -1):
                ans = (ans + go(i - 1, target - j)) % MOD
            cache[i][target] = ans
            has_cache[i][target] = True
            return ans

        return go(n, target)


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfDiceRollsWithTargetSum(Solution):
    pass
