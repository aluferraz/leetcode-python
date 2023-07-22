from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def distinctIntegers(self, N):
        """
        :type n: int
        :rtype: int
        """

        board = [0 for _ in range(N + 1)]

        def place(x):
            if board[x] != 0:
                return
            for i in range(1, x + 1):
                if x % i == 1:
                    place(i % x)
            board[x] = 1

        place(N)
        return sum(board)


# leetcode submit region end(Prohibit modification and deletion)


class CountDistinctNumbersOnBoard(Solution):
    pass
