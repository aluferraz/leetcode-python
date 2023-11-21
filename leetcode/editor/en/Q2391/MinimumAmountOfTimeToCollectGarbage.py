import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        N = len(garbage)

        counter = collections.defaultdict(int)

        for i in range(N):
            cnt_row = collections.defaultdict(int)
            for c in garbage[i]:
                cnt_row[c] += 1
            counter[(i, 'P')] = cnt_row['P']
            counter[(i, 'M')] = cnt_row['M']
            counter[(i, 'G')] = cnt_row['G']

        travel.append(0)

        def go(i, t, b):
            if i == N:
                return 0
            key = (i, t)
            if counter[key] > 0:
                return counter[key] + b + go(i + 1, t, travel[i])
            return go(i + 1, t, b + travel[i])

        ans = 0

        ans += go(0, 'P', 0)
        ans += go(0, 'M', 0)
        ans += go(0, 'G', 0)
        return ans


class MinimumAmountOfTimeToCollectGarbage(Solution):
    pass
