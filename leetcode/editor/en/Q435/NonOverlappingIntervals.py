from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        INF = 10 ** 20
        ending_at = -INF
        non_overlapping = 0
        N = len(intervals)
        for s, e in intervals:
            if s >= ending_at:
                non_overlapping += 1
                ending_at = e
            else:
                ending_at = min(ending_at, e)

        return N - non_overlapping


# leetcode submit region end(Prohibit modification and deletion)


class NonOverlappingIntervals(Solution):
    pass
