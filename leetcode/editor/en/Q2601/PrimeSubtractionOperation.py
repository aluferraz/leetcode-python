import math
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)

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


primes = prime_sieve(10 ** 6)


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        N = len(nums)
        global primes

        def find(minimum):
            left = 0
            right = len(primes)
            ans = -1
            while left < right:
                mid = (left + right) // 2
                if primes[mid] >= minimum:
                    right = mid
                else:
                    ans = mid
                    left = mid + 1
            if ans == -1:
                return 0
            return primes[ans]

        max_seen = 0
        for i in range(N):
            nums[i] -= find(nums[i] - max_seen)
            max_seen = max(max_seen, nums[i])

        return nums == sorted(nums) and len(nums) == len(set(nums))


# leetcode submit region end(Prohibit modification and deletion)


class PrimeSubtractionOperation(Solution):
    pass
