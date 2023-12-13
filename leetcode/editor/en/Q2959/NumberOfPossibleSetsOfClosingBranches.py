import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numberOfSets(self, n, maxDistance, roads):
        """
        :type n: int
        :type maxDistance: int
        :type roads: List[List[int]]
        :rtype: int
        """
        N = n
        roads.sort(key=lambda x: x[2])
        left = 0
        right = 0
        total_distance = 0
        edges = [0] * N
        branches = 0
        ans = set()
        ans.add(0)
        while right < len(roads):
            while left < right and total_distance + roads[right][2] > maxDistance:
                total_distance -= roads[left][2]
                edges[roads[left][1]] -= 1
                edges[roads[left][0]] -= 1
                if edges[roads[left][1]] == 0:
                    branches &= (~(1 << roads[left][1]))
                if edges[roads[left][0]] == 0:
                    branches &= (~(1 << roads[left][0]))
                ans.add(branches)
                left += 1
            if roads[right][2] > maxDistance:
                break
            total_distance += roads[right][2]
            if total_distance <= maxDistance:
                branches |= (1 << roads[right][1])
                branches |= (1 << roads[right][0])
                edges[roads[right][1]] += 1
                edges[roads[right][0]] += 1
                ans.add(branches)
            right += 1
        while left < right:
            total_distance -= roads[left][2]
            edges[roads[left][1]] -= 1
            edges[roads[left][0]] -= 1
            if edges[roads[left][1]] == 0:
                branches &= (~(1 << roads[left][1]))
            if edges[roads[left][0]] == 0:
                branches &= (~(1 << roads[left][0]))
            ans.add(branches)
            left += 1
        return len(ans) + (N + 1)


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfPossibleSetsOfClosingBranches(Solution):
    pass
