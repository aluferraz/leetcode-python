import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        timeline = []
        START = 1
        END = -1
        for s, e in intervals:
            timeline.append((s, START))
            timeline.append((e, END))
        heapq.heapify(timeline)

        rooms_available = 0
        rooms_needed = 0
        while len(timeline) > 0:
            _, evt = heapq.heappop(timeline)
            if evt == START:
                if rooms_available == 0:
                    rooms_needed += 1
                else:
                    rooms_available -= 1
            else:
                rooms_available += 1

        return rooms_needed


# leetcode submit region end(Prohibit modification and deletion)


class MeetingRoomsIi(Solution):
    pass
