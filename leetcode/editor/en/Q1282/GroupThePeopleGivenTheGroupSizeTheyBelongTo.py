import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        workinggroups = collections.defaultdict(list)
        ans = []

        N = len(groupSizes)
        for i in range(N):
            group = groupSizes[i]
            workinggroups[group].append(i)
            if len(workinggroups[group]) == group:
                ans.append(workinggroups.pop(group))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class GroupThePeopleGivenTheGroupSizeTheyBelongTo(Solution):
    pass
