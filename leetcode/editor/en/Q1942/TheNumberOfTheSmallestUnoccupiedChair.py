import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        timeline = []
        START = 0
        END = -1

        N = len(times)
        for i in range(N):
            a, l = times[i]
            timeline.append((a, START, i))
            timeline.append((l, END, i))
        heapq.heapify(timeline)
        chairs_available = []
        chairs_occupied = {}
        next_chair = 0

        while len(timeline):
            time, evt, i = heapq.heappop(timeline)
            if evt == START:
                if len(chairs_available) > 0:
                    chairs_occupied[i] = heapq.heappop(chairs_available)
                else:
                    chairs_occupied[i] = next_chair
                    next_chair += 1
            else:
                used_chair = chairs_occupied[i]
                chairs_occupied.pop(i)
                heapq.heappush(chairs_available, used_chair)
            if i == targetFriend:
                return chairs_occupied[i]
        return -1


# leetcode submit region end(Prohibit modification and deletion)


class TheNumberOfTheSmallestUnoccupiedChair(Solution):
    pass
