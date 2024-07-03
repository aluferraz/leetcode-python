from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        N = len(arr)
        def go(i):
            if i >= N-2:
                return False
            for j in range(i, i+3):
                if arr[i] % 2 == 0:
                    return go(i+1)
            return True
        return go(0)

# leetcode submit region end(Prohibit modification and deletion)


class ThreeConsecutiveOdds(Solution):
    pass
    