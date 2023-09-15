import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        tickets.sort()
        adj_list = collections.defaultdict(collections.deque)

        N = len(tickets)

        for i in range(N):
            f, t = tickets[i]
            adj_list[f].append((t, i))

        ans = []

        def go(airport, used):
            ans.append(airport)
            if used == ((1 << N) - 1):
                return True
            if len(adj_list[airport]) == 0:
                ans.pop()
                return False
            for next_airport, i in adj_list[airport]:
                if used & (1 << i) == 0:
                    if go(next_airport, used | (1 << i)):
                        return True
            ans.pop() #invalid path
            return False

        go("JFK", 0)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class ReconstructItinerary(Solution):
    pass
