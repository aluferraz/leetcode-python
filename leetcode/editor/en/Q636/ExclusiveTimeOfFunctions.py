import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exclusiveTime(self, N: int, logs: List[str]) -> List[int]:
        timeline = []
        START = 1
        END = -1

        for log in logs:
            eid, evt, timestamp = log.split(":")
            if evt == "start":
                timeline.append((int(timestamp), START, int(eid)))
            else:
                timeline.append((int(timestamp) + 1, END, int(eid)))
        heapq.heapify(timeline)

        starts = {}
        last_end = 0
        state = 0
        exclusive_times = [0] * N
        ids_stack = []
        processing_start = 0
        while len(timeline) > 0:
            timestamp, evt, eid = heapq.heappop(timeline)
            if evt == START:
                if len(ids_stack) > 0:
                    # accounting exclusive time
                    previous_eid = ids_stack[-1]
                    exclusive_times[previous_eid] += timestamp - processing_start
                starts[eid] = timestamp
                ids_stack.append(eid)
                state += 1
            elif evt == END:
                exclusive_times[eid] += (timestamp - processing_start)
                ids_stack.pop()
            processing_start = max(processing_start, timestamp)
        return exclusive_times


# leetcode submit region end(Prohibit modification and deletion)


class ExclusiveTimeOfFunctions(Solution):
    pass
