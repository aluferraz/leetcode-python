import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        N = len(board)
        M = len(board[0])
        DIRECTIONS = [
            (1, 0),
            (-1, 0),
            (0, -1),
            (0, 1)
        ]

        pop_queue = []

        def pop_equal():
            keep_trying = True
            while keep_trying:
                for j in range(M):
                    pop_down(j)
                for i in range(N):
                    pop_right(i)
                keep_trying = len(pop_queue) > 0
                dequeue_pop()

        def isValidIdx(i, j):
            return i >= 0 and i < N and j >= 0 and j < M

        def get_upper(i, j):
            if not isValidIdx(i, j):
                return 0
            if board[i][j] >= 0:
                ret_value = board[i][j]
                board[i][j] = get_upper(i - 1, j)
                return ret_value
            else:
                board[i][j] = get_upper(i - 1, j)
                return board[i][j]

        def dequeue_pop():
            pop_queue.sort(key=lambda x: (x[0], x[1]))

            while len(pop_queue) > 0:
                i, j = pop_queue.pop()
                if board[i][j] >= 0:
                    continue
                get_upper(i, j)

        def enqueue_pop(coords):
            i, j = coords
            if board[i][j] == 0:
                return
            board[i][j] = -abs(board[i][j])
            pop_queue.append((i, j))

        def pop_right(row):
            left = 0
            right = 0
            window = collections.deque()
            while right < M:
                if abs(board[row][right]) == abs(board[row][left]):
                    window.append((row, right))
                    right += 1
                    continue
                else:
                    if len(window) >= 3:
                        while len(window) > 0:
                            enqueue_pop(window.popleft())
                            left += 1
                    else:
                        window.clear()
                        left = right
            if len(window) >= 3:
                while len(window) > 0:
                    enqueue_pop(window.popleft())
                    left += 1

        def pop_down(col):
            left = 0
            right = 0
            window = collections.deque()
            while right < N:
                if abs(board[right][col]) == abs(board[left][col]):
                    window.append((right, col))
                    right += 1
                    continue
                else:
                    if len(window) >= 3:
                        while len(window) > 0:
                            enqueue_pop(window.popleft())
                            left += 1
                    else:
                        window.clear()
                        left = right
            if len(window) >= 3:
                while len(window) > 0:
                    enqueue_pop(window.popleft())
                    left += 1

        pop_equal()
        return board


# leetcode submit region end(Prohibit modification and deletion)


class CandyCrush(Solution):
    pass
