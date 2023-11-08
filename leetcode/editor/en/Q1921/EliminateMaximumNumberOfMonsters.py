import math

import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        N = len(dist)
        if N == 1:
            return N
        # normalized_dist = [0] * N
        # for i in range(N):
        #     normalized_dist[i] = dist[i] // speed[i]
        # normalized_dist.sort()
        combined = list(zip(dist, speed))
        combined.sort(key=lambda x: math.ceil(x[0] / x[1]))

        ans = 0
        target_idx = 0
        i = 0
        while target_idx < N:
            real_dist = combined[target_idx][0] - (i * combined[target_idx][1])
            if real_dist <= 0:
                break
            target_idx += 1
            ans += 1
            i += 1
        return ans
    # leetcode submit region end(Prohibit modification and deletion)


class EliminateMaximumNumberOfMonsters(Solution):
    pass
