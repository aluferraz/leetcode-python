import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def relocateMarbles(self, nums, moveFrom, moveTo):
        """
        :type nums: List[int]
        :type moveFrom: List[int]
        :type moveTo: List[int]
        :rtype: List[int]
        """
        states = collections.defaultdict(int)
        for pos in nums:
            states[pos] += 1

        N = len(moveFrom)
        for i in range(N):
            fPos = moveFrom[i]
            tPos = moveTo[i]
            if fPos == tPos:
                continue
            if states[fPos] > 0:
                states[tPos] += states[fPos]
            states.pop(fPos)

        return sorted(states.keys())


# leetcode submit region end(Prohibit modification and deletion)


class RelocateMarbles(Solution):
    pass
