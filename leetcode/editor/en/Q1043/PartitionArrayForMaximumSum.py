from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        N = len(arr)
        INF = 10**20
        cache = {}
        def go(i, t, m):
            if i == N:
                return 0
            if (i,t) in cache:
                 return cache[(i,t,m)]
            m = max(m, arr[i])
            best_ahead = go(i+1, 1, -INF)

            break_here = (m * t) + best_ahead
            keep_going = -INF
            if t < k:
                keep_going = go(i+1, t+1, m)
            ans = max(break_here, keep_going)
            cache[(i,t,m)] = ans
            return ans

        ans = go(0,1, -INF)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class PartitionArrayForMaximumSum(Solution):
    pass