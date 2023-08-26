import math
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        upper = max(nums)

        def prime_sieve(n):
            primes = [True for _ in range(n + 1)]
            primes[0] = False
            primes[1] = False

            limit = int(math.sqrt(n))
            for i in range(2, limit + 1):
                if primes[i]:
                    j = 2
                    while j * i <= n:
                        primes[j * i] = False
                        j += 1
            ans = [
                i for i in range(len(primes)) if primes[i]
            ]
            return ans

        primes = prime_sieve(upper)

        def get_score(n):
            divisors = set()
            current = n
            while current != 1:
                for p in primes:
                    if current % p == 0:
                        divisors.add(p)
                        current /= p
                        break
            return len(divisors)

        N = len(nums)
        score_arr = [0] * N
        for i in range(N):
            score_arr[i] = get_score(nums[i])
        print(score_arr)


# leetcode submit region end(Prohibit modification and deletion)


class ApplyOperationsToMaximizeScore(Solution):
    pass
