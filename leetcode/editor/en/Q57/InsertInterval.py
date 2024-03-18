import heapq
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        intervals.append(newInterval)
        intervals.sort()
        ans = []

        for s,e in intervals:
            if len(ans) > 0 and ans[-1][-1] >= s:
                ans[-1][-1] = max(e,ans[-1][-1])
                continue
            ans.append([s,e])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class InsertInterval(Solution):
    pass