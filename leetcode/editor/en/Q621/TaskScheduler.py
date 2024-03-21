import collections
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        timeline = []
        pool = []
        cnts = collections.Counter(tasks).values()
        for c in cnts:
            timeline.append((0, c))
        heapq.heapify(timeline)
        current_time = 0

        while len(timeline) > 0 or len(pool) > 0:
            if len(pool) == 0:
                time = timeline[0][0]
                current_time = max(current_time, time)
            while len(timeline) > 0 and current_time >= (t := timeline[0][0]):
                t,cnt = heapq.heappop(timeline)
                if cnt > 0:
                    heapq.heappush(pool, -cnt)
            current_time += 1
            c = abs(heapq.heappop(pool))
            if c > 1:
                heapq.heappush(timeline,(current_time + n, c - 1))
        return current_time

# leetcode submit region end(Prohibit modification and deletion)


class TaskScheduler(Solution):
    pass
