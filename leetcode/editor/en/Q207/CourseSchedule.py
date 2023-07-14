import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        start = []
        in_degree = [0 for _ in range(numCourses)]
        adj_list = collections.defaultdict(list)
        for u, v in prerequisites:
            in_degree[u] += 1
            adj_list[v].append(u)

        for i in range(numCourses):
            if in_degree[i] == 0:
                start.append(i)

        if len(start) == 0:
            return False

        cache = [None for _ in range(numCourses)]
        stack = set()

        def dfs(i):
            if i in stack:
                cache[i] = False
            if cache[i] is not None:
                return cache[i]
            stack.add(i)
            for edge in adj_list[i]:
                if not dfs(edge):
                    cache[i] = False
                    return False
            cache[i] = True
            stack.remove(i)
            return cache[i]

        for node in start:
            dfs(node)

        for i in range(numCourses):
            if not cache[i]:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)


class CourseSchedule(Solution):
    pass
