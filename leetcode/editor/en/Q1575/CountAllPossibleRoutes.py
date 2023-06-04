# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):

    def countRoutes(self, locations, start, finish, fuel):
        """
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        """
        MOD = (10 ** 9) + 7
        N = len(locations)
        dp = [[False for _ in range(N)] for _ in range(fuel + 1)]

        for f in range(fuel + 1):
            for i in range(N):
                costToFinish = abs(locations[i] - locations[finish])
                dp[f][i] = costToFinish <= f

        cache = {}

        def count(start, finish, fuel):
            ans = 0
            if start == finish:
                ans += 1
            if ((start, fuel) in cache):
                return cache[(start, fuel)]
            for i in range(N):
                if i == start:
                    continue
                cost = abs(locations[i] - locations[start])
                remaining = fuel - cost
                if remaining >= 0 and dp[remaining][i]:  # If jumping to "i" is possible and "i" can jump to finish
                    ans = (ans + count(i, finish, remaining)) % MOD
            cache[(start, fuel)] = ans % MOD
            return cache[(start, fuel)]

        return count(start, finish, fuel)


# leetcode submit region end(Prohibit modification and deletion)


class CountAllPossibleRoutes(Solution):
    pass
