from math import ceil
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        N = len(dist)
        longest_dist = max(dist)

        # find the closest integer

        def good_integer(div, target):
            time = 0
            for i in range(N):
                arrival_time = (dist[i] / div)
                waiting_time = 0
                if i < N - 1:
                    waiting_time = ceil(time + arrival_time) - (time + arrival_time)
                time += arrival_time + waiting_time
                if time > target:
                    return False
            return time <= target

        def closest_integer_hour(target):
            left = 1
            right = (longest_dist + 1) * 100
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if good_integer(mid, target):
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans

        return closest_integer_hour(hour)


# leetcode submit region end(Prohibit modification and deletion)


class MinimumSpeedToArriveOnTime(Solution):
    pass
