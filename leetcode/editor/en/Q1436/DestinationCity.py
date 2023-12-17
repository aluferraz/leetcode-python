import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        adj_list = collections.defaultdict(list)
        for u, v in paths:
            adj_list[u].append(v)
            if v not in adj_list:
                adj_list[v] = list()

        for k, v in adj_list.items():
            if len(v) == 0:
                return k
        return ""


# leetcode submit region end(Prohibit modification and deletion)


class DestinationCity(Solution):
    pass
