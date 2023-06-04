import collections
import heapq
from typing import List


class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def digsum(n):
            ans = 0
            for i in range(len(n)):
                ans += int(n[i])
            return ans

        ans = 0
        left = int(num1)
        right = int(num2)
        minGood = right
        for num in range(left, right + 1):
            dsum = digsum(str(num))
            if dsum >= min_sum and dsum <= max_sum:
                minGood = num
                break

        num = minGood
        startLen = len(str(minGood))

        ansCache = collections.defaultdict(int)

        while len(str(num)) == startLen:
            dsum = digsum(str(num))
            if dsum >= min_sum and dsum <= max_sum:
                ans += 1
            ansCache[num] = ans
            num += 1
        boundary = len(num2) - startLen
        if boundary > 0:
            ans *= boundary
            rest = int(num2) % 10
            ans += ansCache[rest + 1]

        return ans
