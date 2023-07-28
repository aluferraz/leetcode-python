import collections
import heapq
from typing import List

import sortedcontainers


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxRunTime(self, N, batteries):
        """
        :type N: int
        :type batteries: List[int]
        :rtype: int
        """
        best = sum(batteries)
        M = len(batteries)
        batteries.sort()
        computers = collections.deque()

        for i in range(N):
            computers.appendleft(batteries.pop())

        remaining = sum(batteries[:M - N])

        def find_computers(target):
            left = 0
            right = N - 1
            ans = right
            while left <= right:
                mid = (left + right) // 2
                if computers[mid] < target:
                    left = mid + 1
                else:
                    ans = mid
                    right = mid - 1
            return ans

        def can_reach(target):

            computers_idx = find_computers(target)
            can_use = remaining
            i = 0
            while i <= computers_idx:
                if computers[i] >= target:
                    break
                can_use -= target - computers[i]
                i += 1
            return can_use >= 0

        left = 0
        right = best + 1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if can_reach(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

    # leetcode submit region end(Prohibit modification and deletion)


class MaximumRunningTimeOfNComputers(Solution):
    pass
