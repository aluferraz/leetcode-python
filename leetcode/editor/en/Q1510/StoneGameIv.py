import collections
import math
from functools import cache
from math import sqrt
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def winnerSquareGame(self, N):
        """
        :type n: int
        :rtype: bool
        """
        if N == 0:
            return False
        stones = []

        for i in range(1, N + 1):
            if (sqrt(i) == int(sqrt(i))):
                stones.append(i)

        cache = {}

        def find(target):
            left = 0
            right = len(stones)
            while left < right:
                mid = (left + right) // 2
                if stones[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return min(left, len(stones) - 1)

        def canWin(player, remaining):
            if remaining in stones:
                cache[remaining] = True
                return True
            if remaining in cache:
                return cache[remaining]
            startIdx = find(remaining)
            for i in range(startIdx, -1, -1):
                s = stones[i]
                if s > remaining:
                    continue
                if not canWin((player + 1) % 2, remaining - s):
                    cache[remaining] = True
                    return True
            cache[remaining] = False
            return False

        return canWin(0, N)


# leetcode submit region end(Prohibit modification and deletion)


class StoneGameIv(Solution):
    pass
