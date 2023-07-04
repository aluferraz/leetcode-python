import collections
import heapq
import math
from functools import cache
from math import gcd
from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        N = len(positions)

        timeline = []
        for i in range(N):
            dire = -1 if directions[i] == 'R' else 1
            timeline.append((positions[i], dire, healths[i], i))

        timeline.sort(key=lambda x: (x[0], x[1]))

        ans = collections.deque()
        ans.append(timeline[0])

        for i in range(1, N):
            if len(ans) >= 1:
                (position, dire, health, j) = timeline[i]
                (prevPosition, prevDire, prevHealth, k) = ans[- 1]
                if dire == prevDire or prevDire == 1 and dire == -1:
                    ans.append(timeline[i])
                else:
                    remaining = health
                    while remaining > 0 and len(ans) > 0 and prevDire == -1 and prevPosition < position:
                        if remaining > prevHealth:
                            remaining -= 1
                        elif remaining < prevHealth:
                            remaining = -1
                        else:
                            remaining = 0
                        ans.pop()
                        if len(ans) > 0 and remaining > 0:
                            (prevPosition, prevDire, prevHealth, k) = ans[-1]
                    if remaining > 0:
                        ans.append((position, dire, remaining, j))
                    elif remaining < 0:
                        ans.append((prevPosition, prevDire, prevHealth - 1, k))
            else:
                ans.append(timeline[i])

        ans = list(ans)
        ans.sort(key=lambda x: x[3])

        final = []

        for (position, dire, health, j) in ans:
            final.append(health)
        return final
