from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        hours = {}
        for t in timePoints:
            h, m = t.split(':')
            hour = int(h)
            minute = int(m)
            if hour not in hours:
                hours[hour] = []
            hours[hour].append(minute)

        ans = 10 ** 20
        keys = hours.keys()
        for i in keys:
            hours[i].sort()
        for i in keys:
            for j in range(1, len(hours[i])):
                ans = min(ans, hours[i][j] - hours[i][j - 1])
            for k in range(1, 24):
                next_hour = (i + k) % 24
                if next_hour in hours:
                    first_min = hours[next_hour][0]
                    ans = min(ans, (((k * 60) - hours[i][-1]) + first_min))
                    break
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MinimumTimeDifference(Solution):
    pass
