import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def totalNQueens(self, N):
        """
        :type N: int
        :rtype: int
        """
        forbidden = collections.defaultdict(int)

        def set_queen(i, j, place):

            # k_back = j - 1
            # k_front = j + 1
            # for i in range(i - 1, -1, -1):
            #
            #     if place:
            #         forbidden.add((i, k_back))
            #     else:
            #         forbidden.discard((i, k_back))
            #     k_back -= 1
            #     if place:
            #         forbidden.add((i, k_front))
            #     else:
            #         forbidden.discard((i, k_front))
            #     k_front += 1
            #     if place:
            #         forbidden.add((i, j))
            #     else:
            #         forbidden.discard((i, j))

            k_back = j - 1
            k_front = j + 1
            for i in range(i + 1, N):
                if k_back >= 0:
                    if place:
                        forbidden[(i, k_back)] += 1
                    else:
                        forbidden[(i, k_back)] -= 1
                    k_back -= 1
                if k_front < N:
                    if place:
                        forbidden[(i, k_front)] += 1
                    else:
                        forbidden[(i, k_front)] -= 1
                    k_front += 1
                if place:
                    forbidden[(i, j)] += 1
                else:
                    forbidden[(i, j)] -= 1

        def go(i):
            if i == N:
                return 1
            ans = 0
            for j in range(N):
                if forbidden[(i, j)] > 0:
                    continue
                set_queen(i, j, True)
                ans += go(i + 1)
                set_queen(i, j, False)

            return ans

        return go(0)


# leetcode submit region end(Prohibit modification and deletion)


class NQueensIi(Solution):
    pass
