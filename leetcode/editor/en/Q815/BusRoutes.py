import collections
from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if source == target:
            return 0
        stops = collections.defaultdict(set)
        N = len(routes)

        indexesMap = {}

        for i in range(N):
            M = len(routes[i])
            # for bus in routes[i]:
            for j in range(M):
                bus = routes[i][j]
                stops[bus].add(i)
                indexesMap[(i, bus)] = j
            routes[i] += routes[i]

        INF = 10 ** 20
        targetGroups = set()

        for g in stops[target]:
            targetGroups.add(g)

        def bfs():
            visited = set()  # Tracks visited groups
            busses = set()  # Tracks visited groups
            queue = collections.deque()  # Queue for BFS

            # Initial queue setup
            for g in stops[source]:
                queue.append((g, indexesMap[(g, source)], 0))

            while len(queue) > 0:
                group, busIdx, dist = queue.popleft()
                if group in visited:
                    continue
                visited.add(group)
                bus = routes[group][busIdx]

                if bus == target:
                    return dist

                if group in targetGroups:
                    return dist + 1

                for i in range(busIdx + 1, len(routes[group])):
                    busStop = routes[group][i]
                    if busStop == target:
                        return dist + 1
                    if busStop in busses:
                        continue
                    busses.add(busStop)
                    for g in stops[busStop]:
                        if g != group and g not in visited:
                            queue.append((g, indexesMap[(g, busStop)], dist + 1))

            return INF

        ans = bfs()
        return ans if ans < INF else -1

        # leetcode submit region end(Prohibit modification and deletion)


class BusRoutes(Solution):
    pass
