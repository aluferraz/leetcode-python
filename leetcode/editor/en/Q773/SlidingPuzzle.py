import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        N = len(board)
        M = len(board[0])

        def good(matrix):
            return matrix == [[1, 2, 3], [4, 5, 0]]

        def cache_key(matrix):
            return "".join("".join(str(x) for x in y) for y in matrix)

        def is_valid(i, j):
            return i >= 0 and i < N and j >= 0 and j < M

        def get_pos(matrix):
            for i in range(N):
                for j in range(M):
                    if matrix[i][j] == 0:
                        return i, j
            return -1, -1

        if good(board):
            return 0
        DIRECTIONS = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        cache = set()

        q = collections.deque()
        i, j = get_pos(board)
        q.append(([list(board[0]), list(board[1])], i, j, 0))

        while q:
            size = len(q)
            for _ in range(size):
                bhere, i, j, moves = q.popleft()
                for di, dj in DIRECTIONS:
                    ni, nj = (i + di, j + dj)
                    if is_valid(ni, nj):
                        bhere[i][j] = bhere[ni][nj]
                        bhere[ni][nj] = 0
                        if cache_key(bhere) not in cache:
                            if good(bhere):
                                return moves + 1
                            cache.add(cache_key(bhere))
                            q.append(([list(bhere[0]), list(bhere[1])], ni, nj, moves + 1))
                        bhere[ni][nj] = bhere[i][j]
                        bhere[i][j] = 0

        return -1


# leetcode submit region end(Prohibit modification and deletion)


class SlidingPuzzle(Solution):
    pass
