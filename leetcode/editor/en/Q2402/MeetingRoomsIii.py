import collections
import heapq
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [(-1,i) for i in range(n)]
        START = 1
        END = -1
        timeline = []
        counter = collections.defaultdict(int)
        delays = collections.defaultdict(int)
        meetings_map = {}
        for i in range(len(meetings)):
            s,e = meetings[i]
            timeline.append((START, s,i))
            timeline.append((END, e, i))
            meetings_map[i] = (s,e)
        heapq.heapify(timeline)
        heapq.heapify(rooms)

        while len(timeline) > 0:
            evt, time, id = heapq.heappop(timeline)
            if evt == END:
                if id in delays:
                    timeline.append((END, time + delays[id], id))
            else:
                if rooms[0][0] > time:
                    delay = rooms[0][0] - time
                    timeline.append((START, time + delay, id))
                    delays[id] = delay

                rtime, rid = heapq.heappop(rooms)
                counter[rid] += 1
                rtime = meetings_map[id][1]
                heapq.heappush(rooms, (rtime, rid))

        ans = 0
        ans_room = 0
        for i in range(n):
            if counter[i] > ans:
                ans = counter[i]
                ans_room = i
        return ans_room



# leetcode submit region end(Prohibit modification and deletion)


class MeetingRoomsIii(Solution):
    pass