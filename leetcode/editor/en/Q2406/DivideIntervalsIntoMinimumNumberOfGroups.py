from typing import List

import sortedcontainers


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        groups = sortedcontainers.SortedList(key=lambda x: x[-1])
        groups.add([0])

        def find(start):
            left = 0
            right = len(groups)
            ans = len(groups)
            while left < right:
                mid = (left + right) // 2
                if groups[mid][-1] >= start:
                    right = mid
                else:
                    ans = mid
                    left = mid + 1
            return ans

        for s, e in intervals:
            idx = find(s)
            if idx == len(groups):
                groups.add([e])
            else:
                group = groups[idx]
                group.append(e)
                groups.pop(idx)
                groups.add(group)

        return len(groups)


# leetcode submit region end(Prohibit modification and deletion)


class DivideIntervalsIntoMinimumNumberOfGroups(Solution):
    pass
