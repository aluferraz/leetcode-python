from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        N = len(board)
        M = len(board[0])

        def isValidIdx(i, j):
            return i >= 0 and i < N and j >= 0 and j < M

        DIRECTIONS = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (-1, -1),
            (-1, 1),
            (1, 1),
            (1, -1),
        ]

        def get_info(i, j):
            alive = 0
            dead = 0

            for u, v in DIRECTIONS:
                if not isValidIdx(i + u, j + v):
                    continue
                if board[i + u][j + v] == 1:
                    alive += 1
                else:
                    dead += 1
            return (alive, dead)

        changes = {}

        for i in range(N):
            for j in range(M):
                (alive, dead) = get_info(i, j)
                if board[i][j] == 1:
                    if alive < 2:
                        # board[i][j] = 0
                        changes[(i, j)] = 0
                    # elif (alive >= 2 and alive <= 3):
                    # board[i][j] = 1
                    elif alive > 3:
                        # board[i][j] = 0
                        changes[(i, j)] = 0
                else:
                    if alive == 3:
                        # board[i][j] = 1
                        changes[(i, j)] = 1
        for (i, j) in changes:
            board[i][j] = changes[(i, j)]
        return board


# leetcode submit region end(Prohibit modification and deletion)


class GameOfLife(Solution):
    pass
