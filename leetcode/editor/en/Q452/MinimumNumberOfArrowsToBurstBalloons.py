import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        timeline = []
        START = -1
        END = 1
        N = len(points)
        for i in range(N):
            s, e = points[i]
            timeline.append((s, START, i))
            timeline.append((e, END, i))
        heapq.heapify(timeline)
        state = 0
        ans = 0
        shot = [False] * N
        ids = []
        while len(timeline) > 0:
            t, evt, id = heapq.heappop(timeline)
            if evt == START:
                ids.append(id)
            elif not shot[id]:
                needed = 1
                while len(ids) > 0:
                    id = ids.pop()
                    shot[id] = True
                ans += needed

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MinimumNumberOfArrowsToBurstBalloons(Solution):
    pass
