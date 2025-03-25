import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        N = len(meetings)
        timeline = []
        end_time = 0
        start_time = days
        START = 0
        END = -1
        for s, e in meetings:
            e += 1
            timeline.append((s, START))
            timeline.append((e, END))
            end_time = max(end_time, e - 1)
            start_time = min(start_time, s)
        heapq.heapify(timeline)
        ans = (start_time - 1) + (days - end_time)
        max_end = start_time
        open = 0
        while timeline:
            time, event = heapq.heappop(timeline)
            if event == END:
                max_end = max(time, max_end)
                open -= 1
            else:
                if time > max_end and open == 0:
                    ans += (time - max_end)
                open += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class CountDaysWithoutMeetings(Solution):
    pass
