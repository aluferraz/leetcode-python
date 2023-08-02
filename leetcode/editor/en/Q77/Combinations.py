from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        ans = []

        def go(start, k, running):
            if k == 0:
                ans.append(list(running))
                return
            for i in range(start, n + 1):
                running.append(i)
                go(i + 1, k - 1, running)
                running.pop()

        go(1, k, [])

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class Combinations(Solution):
    pass
