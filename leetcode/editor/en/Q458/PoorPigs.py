import math

import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        # https://www.youtube.com/watch?v=9YSHcsprxh0
        if buckets <= 1:
            return 0
        if buckets == 2:
            return 1
        maximum_turns = minutesToTest // minutesToDie

        pigs = 0
        dimension_search = (maximum_turns + 1) ** pigs
        while dimension_search < buckets:
            pigs += 1
            dimension_search = (maximum_turns + 1) ** pigs
        return pigs

        # leetcode submit region end(Prohibit modification and deletion)


class PoorPigs(Solution):
    pass
