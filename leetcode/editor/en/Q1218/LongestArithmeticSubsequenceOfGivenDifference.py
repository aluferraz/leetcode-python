import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        N = len(arr)
        best = collections.defaultdict(int)

        def go(i):
            if i < 0:
                return 0
            value = arr[i]
            best[value] = max(best[value], 1 + best[(value + difference)])
            return max(best[value], go(i - 1))

        return go(N - 1)

        # leetcode submit region end(Prohibit modification and deletion)


class LongestArithmeticSubsequenceOfGivenDifference(Solution):
    pass
