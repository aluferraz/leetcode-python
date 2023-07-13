import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def eventualSafeNodes(self, adj_list):
        """
        :type adj_list: List[List[int]]
        :rtype: List[int]
        """

        N = len(adj_list)

        stack = set()

        cache = {}

        def dfs(i):
            if len(adj_list[i]) == 0:
                cache[i] = True
                return True
            if i in stack:
                cache[i] = False
                return False
            if i in cache:
                return cache[i]
            stack.add(i)
            for edge in adj_list[i]:
                if not dfs(edge):
                    cache[i] = False
                    stack.discard(i)
                    return cache[i]
            cache[i] = True
            stack.discard(i)
            return cache[i]

        for i in range(N):
            dfs(i)

        ans = []
        for i in range(N):
            if cache[i]:
                ans.append(i)
        return ans

        # leetcode submit region end(Prohibit modification and deletion)


class FindEventualSafeStates(Solution):
    pass
