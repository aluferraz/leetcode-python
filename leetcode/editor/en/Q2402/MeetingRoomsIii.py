import collections
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        START = 1
        END = -1
        timeline = []
        counter = collections.defaultdict(int)
        meetings_map = {}
        meetings_prio = []
        for i in range(len(meetings)):
            s, e = meetings[i]
            meetings_map[i] = [s, e, -1]
            meetings_prio.append((s, e, i))
        heapq.heapify(meetings_prio)

        free_rooms = [i for i in range(n)]
        for rid in range(n):
            s, e, i = heapq.heappop(meetings_prio)
            heapq.heappush(timeline, (s, START, rid, i))
            if len(meetings_prio) == 0:
                break

        while len(timeline) > 0:
            time, evt, rid, id = heapq.heappop(timeline)
            if evt == END:
                heapq.heappush(free_rooms, meetings_map[id][2])
                if len(meetings_prio) > 0:
                    s, e, i = heapq.heappop(meetings_prio)
                    if time > s:
                        delay = time - s
                        duration = e - s
                        s += delay
                        e = s + duration
                    meetings_map[i][0] = s
                    meetings_map[i][1] = e
                    heapq.heappush(timeline, (s, START, rid, i))
            else:
                rid = heapq.heappop(free_rooms)
                counter[rid] += 1
                rtime = meetings_map[id][1]
                meetings_map[id][2] = rid
                heapq.heappush(timeline, (rtime, END, rid, id))

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
