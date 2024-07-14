import heapq
from typing import List

import sortedcontainers


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        N = len(positions)
        right_robots = []
        left_robots = sortedcontainers.SortedList()

        for i in range(N):
            if directions[i] == "R":
                right_robots.append((-positions[i], -healths[i], i))
            if directions[i] == "L":
                left_robots.add((positions[i], -healths[i], i))
        heapq.heapify(right_robots)

        # heapq.heapify(left_robots)
        def find(target):
            left = 0
            right = len(left_robots)
            ans = -1
            while left < right:
                mid = (left + right) // 2
                if left_robots[mid][0] >= target:
                    ans = mid
                    right = mid
                else:
                    left = mid + 1
            return ans

        survivors = []
        while len(right_robots) > 0 and len(left_robots) > 0:
            rpos, rhealth, ridx = right_robots[0]
            lcol_idx = find(abs(rpos))
            if lcol_idx == -1:
                rpos, rhealth, ridx = heapq.heappop(right_robots)
                survivors.append((ridx, rhealth))
                continue
            lpos, lhealth, lidx = left_robots[lcol_idx]
            rhealth = abs(rhealth)
            lhealth = abs(lhealth)
            if lhealth == rhealth:
                heapq.heappop(right_robots)
                left_robots.pop(lcol_idx)
            elif lhealth > rhealth:
                heapq.heappop(right_robots)
                left_robots.pop(lcol_idx)
                lhealth -= 1
                if lhealth > 0:
                    left_robots.add((lpos, -lhealth, lidx))
            elif rhealth > lhealth:
                heapq.heappop(right_robots)
                left_robots.pop(lcol_idx)
                rhealth -= 1
                if rhealth > 0:
                    heapq.heappush(right_robots, (rpos, -rhealth, ridx))

        while right_robots:
            rpos, rhealth, ridx = heapq.heappop(right_robots)
            survivors.append((ridx, rhealth))
        for lpos, lhealth, lidx in left_robots:
            survivors.append((lidx, lhealth))
        survivors.sort()
        ans = []
        for _, health in survivors:
            ans.append(abs(health))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class RobotCollisions(Solution):
    pass
