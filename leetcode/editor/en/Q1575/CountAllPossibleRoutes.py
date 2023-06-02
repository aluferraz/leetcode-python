# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):

    def __init__(self):
        self.cache = collections.defaultdict(lambda: None)

    def countRoutes(self, locations, start, finish, fuel):
        """
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        """
        MOD = (10 ** 9) + 7
        INF = 10 ** 20
        N = len(locations)
        dp = [[0 for _ in range(0, N + 1)] for _ in range(0, fuel + 1)]
        for i in range(0, N):
            dp[0][i] = fuel

        for i in range(0, fuel + 1):
            # for j in range(0, N):
                



        # if self.cache[(start, finish, fuel)] is not None:
        #     return self.cache[(start, finish, fuel)]
        # q = collections.deque()
        # q.append([start, fuel])
        # ans = 0
        # N = len(locations)
        # while len(q) > 0:
        #     size = len(q)
        #     for _ in range(0, size):
        #         info = q.popleft()
        #         node = info[0]
        #         remaining = info[1]
        #
        #         for next_location in range(0, N):
        #             if next_location == node:
        #                 continue
        #             cost = abs(locations[node] - locations[next_location])
        #             fuelRequired = remaining - cost
        #             if fuelRequired >= 0:
        #                 if next_location == finish:
        #                     ans = (ans + 1) % MOD
        #                 else:
        #                     q.append([next_location, fuelRequired])
        #                 fuelBouncing = fuelRequired - abs(locations[next_location] - locations[node])
        #                 if fuelBouncing >= 0:
        #                     ans = (ans + self.countRoutes(locations, node, finish, fuelBouncing)) % MOD
        # ans %= MOD
        # self.cache[(start, finish, fuel)] = ans
        # return ans


# leetcode submit region end(Prohibit modification and deletion)


class CountAllPossibleRoutes(Solution):
    pass
