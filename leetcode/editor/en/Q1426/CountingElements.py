from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        a_set = set(arr)
        ans = 0
        for x in arr:
            if x + 1 in a_set:
                ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class CountingElements(Solution):
    pass
