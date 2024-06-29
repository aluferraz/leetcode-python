import collections
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        adj_list = collections.defaultdict(list)
        for u,v in roads:
            adj_list[u].append(v)
            adj_list[v].append(u)

        keys_sorted = [ (len(y), x) for x,y in adj_list.items() ]
        keys_sorted.sort()

        ans = 0

        while len(keys_sorted) > 0:
            times, city  = keys_sorted.pop()
            ans += (times * n)
            n -= 1
        return ans




# leetcode submit region end(Prohibit modification and deletion)


class MaximumTotalImportanceOfRoads(Solution):
    pass
    