import collections
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumTime(self, n, relations, time):
        """
        :type n: int
        :type relations: List[List[int]]
        :type time: List[int]
        :rtype: int
        """
        N = n
        timeline = []

        START = 1
        END = -1

        unlocks = collections.defaultdict(list)
        dependencies = [0] * (N + 1)

        for prev, cur in relations:
            dependencies[cur] += 1
            unlocks[prev].append(cur)

        current_time = 0

        for i in range(1, N + 1):
            if dependencies[i] == 0:
                heapq.heappush(timeline, (current_time, START, i))
                heapq.heappush(timeline, (current_time + time[i - 1], END, i))

        while len(timeline) > 0:
            evt_time, evt, course = heapq.heappop(timeline)
            current_time = max(current_time, evt_time)
            if evt == END:
                for unlocked in unlocks[course]:
                    dependencies[unlocked] -= 1
                    if dependencies[unlocked] == 0:
                        heapq.heappush(timeline, (evt_time, START, unlocked))
                        heapq.heappush(timeline, (evt_time + time[unlocked - 1], END, unlocked))
        return current_time


# leetcode submit region end(Prohibit modification and deletion)


class ParallelCoursesIii(Solution):
    pass
