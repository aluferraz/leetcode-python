import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = (10 ** 9) + 7
        arr.sort()
        N = len(arr)
        #
        # def getAllDivisors(num):
        #     ans = collections.OrderedDict()
        #     i = 1
        #     while i * i < num:
        #         if num % i == 0:
        #             ans[i] = i
        #         i += 1
        #     while i >= 1:
        #         if num % i == 0:
        #             ans[(num // i)] = i
        #         i -= 1
        #     return ans.keys()

        seen = {}
        has_cache = [False] * N
        cache = [0] * N

        def go(i):
            if i == N:
                return 0
            if has_cache[i]:
                return cache[i]
            # divisors = getAllDivisors(arr[i])
            ans = 1
            for j in range(i):
                d = arr[j]
                if arr[i] % d == 0:
                    if d in seen and (arr[i] // d) in seen:
                        divisor_index = seen[d]
                        division_index = seen[(arr[i] // d)]
                        ans = (
                                      ans +
                                      (1 * go(divisor_index) * go(division_index))
                              ) % MOD

            has_cache[i] = True
            cache[i] = ans % MOD
            seen[arr[i]] = i
            return cache[i]

        ans = 0
        for i in range(N):
            ans = (ans % MOD + go(i) % MOD) % MOD
        return ans % MOD


# leetcode submit region end(Prohibit modification and deletion)


class BinaryTreesWithFactors(Solution):
    pass
