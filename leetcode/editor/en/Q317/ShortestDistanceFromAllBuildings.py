import collections
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        N = len(grid)
        M = len(grid[0])
        INF = 10 ** 20
        def is_valid(i,j):
            return i >= 0 and i < N and j >= 0 and j < M and grid[i][j] < INF

        building_queue = collections.deque()
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    building_queue.append((i,j))
                if grid[i][j]  > 0:
                    grid[i][j] = INF
        buildings = len(building_queue)
        buildings_touched = [[0 for _ in range(M)] for _ in range(N)]


        def calc_dist(starti, startj):
            queue = collections.deque()
            queue.append((starti, startj, 0))
            visited = set()
            visited.add((starti, startj))

            while queue:
                size = len(queue)
                for _ in range(size):
                    i,j, dist = queue.popleft()
                    grid[i][j] = dist+grid[i][j]
                    for di,dj in DIRECTIONS:
                        next_i = i + di
                        next_j = j + dj
                        if is_valid(next_i,next_j) and (next_i,next_j) not in visited:
                            buildings_touched[next_i][next_j] += 1
                            visited.add((next_i, next_j))
                            queue.append((next_i,next_j, dist+1))
        while building_queue:
            bi,bj = building_queue.popleft()
            calc_dist(bi,bj)

        ans = INF
        for i in range(N):
            for j in range(M):
                if not is_valid(i,j) or buildings_touched[i][j] != buildings:
                    continue
                if grid[i][j] == -1:
                    continue
                ans = min(ans, grid[i][j])
        if ans >= INF:
            return -1
        return ans


        
# leetcode submit region end(Prohibit modification and deletion)


class ShortestDistanceFromAllBuildings(Solution):
    pass
    