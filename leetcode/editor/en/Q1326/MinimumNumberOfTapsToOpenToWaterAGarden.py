import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        real_ranges = []

        for i in range(len(ranges)):
            real_ranges.append([
                max(i - ranges[i], 0),
                min(i + ranges[i], n)
            ])

        real_ranges.sort(key=lambda x: (-x[1], x[0]))
        if real_ranges[0][1] != n:
            return -1
        INF = 10 ** 20
        has_cache = [False] * len(real_ranges)
        cache = [INF] * len(real_ranges)

        def go(i):
            if has_cache[i]:
                return cache[i]
            ans = INF
            s, e = real_ranges[i]
            if s == 0:
                return 1
            for j in range(i + 1, len(real_ranges)):
                if real_ranges[j][1] < s:
                    break
                ans = min(ans, 1 + go(j))
            has_cache[i] = True
            cache[i] = ans
            return ans

        ans = go(0)
        if ans >= INF:
            return -1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MinimumNumberOfTapsToOpenToWaterAGarden(Solution):
    pass
