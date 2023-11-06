import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        amax = max(arr)
        queue = collections.deque(arr)
        prev_winner = -1
        consecutive = 0
        while queue[0] != amax:
            first = queue.popleft()
            second = queue.popleft()
            winner = -2
            if first > second:
                queue.appendleft(first)
                queue.append(second)
                winner = first
            else:
                queue.appendleft(second)
                queue.append(first)
                winner = second
            if winner == prev_winner:
                consecutive += 1
            else:
                consecutive = 1
            if consecutive == k:
                return winner
            prev_winner = winner
        return amax


# leetcode submit region end(Prohibit modification and deletion)


class FindTheWinnerOfAnArrayGame(Solution):
    pass
