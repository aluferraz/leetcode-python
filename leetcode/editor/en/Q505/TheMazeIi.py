from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        DIRECTIONS = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        N = len(maze)
        M = len(maze[0])

        def isValidIdx(i, j):
            return i >= 0 and i < N and j >= 0 and j < M and maze[i][j] == 0

        explored = {}
        exploring = set()
        INF = 10 ** 20
        ans = INF

        def explore(i, j, dir):

            if (i, j, dir) in explored:
                return explored[(i, j, dir)]
            best = INF

            exploring.add((i, j, dir))
            new_i, new_j = (i + DIRECTIONS[dir][0]), (j + DIRECTIONS[dir][1])
            if isValidIdx(new_i, new_j):
                best = min(best, 1 + explore(new_i, new_j, dir))
            else:
                # Stoped
                if [i, j] == destination:
                    exploring.discard((i, j, dir))
                    explored[(i, j, dir)] = 0
                    return 0
                for new_dir in range(len(DIRECTIONS)):
                    if new_dir == dir:
                        continue
                    new_i, new_j = (i + DIRECTIONS[new_dir][0]), (j + DIRECTIONS[new_dir][1])
                    if (new_i, new_j, new_dir) in exploring:
                        continue
                    if isValidIdx(new_i, new_j):
                        best = min(best, 1 + explore(new_i, new_j, new_dir))
            exploring.discard((i, j, dir))
            explored[(i, j, dir)] = best
            return best

        for i in range(len(DIRECTIONS)):
            ans = min(ans, explore(start[0], start[1], i))
        if ans >= INF:
            return -1
        return ans


# leetcode submit region end(Prohibit modification and deletion)

class TheMazeIi(Solution):
    pass
