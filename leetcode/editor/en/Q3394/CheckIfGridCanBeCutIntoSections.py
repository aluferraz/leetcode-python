import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def solve(axis):
            START = 0
            END = -1
            timeline = []
            for sx, sy, ex, ey in rectangles:
                if axis == 'X':
                    timeline.append((sx, START))
                    timeline.append((ex, END))
                else:
                    timeline.append((sy, START))
                    timeline.append((ey, END))
            heapq.heapify(timeline)
            state = 0
            count = 0
            while timeline:
                time, event = heapq.heappop(timeline)
                if event == END:
                    state -= 1
                else:
                    state += 1
                if state == 0 and time < n:
                    count += 1  # No conflict
            return count >= 2

        return solve('X') or solve('Y')


# leetcode submit region end(Prohibit modification and deletion)


class CheckIfGridCanBeCutIntoSections(Solution):
    pass
