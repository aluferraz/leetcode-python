import collections
import heapq
from typing import List, Optional

import sortedcontainers


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        N = n
        parents = [-1] * N

        def find(i):
            pathComp = []
            while parents[i] >= 0:
                pathComp.append(i)
                i = parents[i]
            while len(pathComp) > 0:
                parents[pathComp.pop()] = i
            return i

        def union(i,j):
            if i == j:
                return
            if parents[j] < parents[i]:
                return union(j,i)
            parents[i] += parents[j]
            parents[j] = i

        def sortPrio(x):
            personPrio = 1
            if x[0] == firstPerson or x[1] == firstPerson \
                    or x[0] == 0 or x[1] == 0:
                personPrio = 0
            return (x[2], personPrio)

        meetings.sort(key=lambda x: sortPrio(x))
        meetings = collections.deque(meetings)

        union(find(firstPerson),find(0))
        root = find(firstPerson)
        while len(meetings) > 0:
            x,y,t = meetings[0]
            px = find(x)
            py = find(y)
            if px == root or py == root:
                break
            meetings.popleft()

        adj_list = {}

        for x,y,t in meetings:
            if x not in adj_list:
                adj_list[x] = collections.defaultdict(list)
            if y not in adj_list:
                adj_list[y] = collections.defaultdict(list)
            adj_list[x][t].append(y)
            adj_list[y][t].append(x)

        def solve(trusted,t):
            secret_know = collections.deque([trusted])
            while len(secret_know) > 0:
                x = secret_know.popleft()
                if not x in adj_list:
                    continue
                px = find(x)
                for y in adj_list[x][t]:
                    py = find(y)
                    if py != px:
                        union(px,py)
                        secret_know.append(y)




        for x, y, t in meetings:
            px = find(x)
            py = find(y)
            root = find(firstPerson)
            if px == root and py != root:
                union(root, py)
                solve(y,t)
            if py == root and px != root:
                union(root,px)
                solve(x,t)

        ans = []

        for i in range(N):
            if find(i) == find(firstPerson):
                ans.append(i)
        return ans




# leetcode submit region end(Prohibit modification and deletion)


class FindAllPeopleWithSecret(Solution):
    pass