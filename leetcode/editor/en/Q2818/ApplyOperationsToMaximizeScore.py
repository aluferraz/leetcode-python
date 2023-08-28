import collections
import heapq
import math
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)


upper = 10 ** 6


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
scores = {}

class Solution(object):

    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        global primes
        global scores

        def get_score(n):
            if n in scores:
                return scores[n]
            divisors = set()
            current = n
            while current != 1:
                for p in primes:
                    if current % p == 0:
                        divisors.add(p)
                        current /= p
                        break
            scores[n] = len(divisors)
            return len(divisors)

        N = len(nums)
        score_arr = [0] * N
        for i in range(N):
            score_arr[i] = get_score(nums[i])

        def previous_greater_element(arr):
            PGE = [-1] * len(arr)
            stack = collections.deque()
            for i in range(len(arr) - 1, -1, -1):
                while len(stack) > 0 and arr[i] >= arr[stack[-1]]:
                    PGE[stack.pop()] = i
                stack.append(i)
            return PGE

        def next_greater_element(arr):
            NGE = [len(arr)] * len(arr)
            stack = collections.deque()
            for i in range(len(arr)):
                while len(stack) > 0 and arr[i] > arr[stack[-1]]:
                    NGE[stack.pop()] = i
                stack.append(i)
            return NGE

        PGE = previous_greater_element(score_arr)
        NGE = next_greater_element(score_arr)

        contrib_arr = [0] * N

        for i in range(N):
            degree_of_freedom = (i - PGE[i]) * (NGE[i] - i)
            contrib_arr[i] = (-nums[i], degree_of_freedom)
        heapq.heapify(contrib_arr)
        ans = 1
        MOD = 10 ** 9 + 7
        while k > 0:
            n, powtimes = heapq.heappop(contrib_arr)
            n = abs(n)
            powtimes = min(powtimes, k)
            ans *= pow(n, powtimes, MOD)
            ans %= MOD
            k -= powtimes
        return ans % MOD


# leetcode submit region end(Prohibit modification and deletion)


class ApplyOperationsToMaximizeScore(Solution):
    pass
