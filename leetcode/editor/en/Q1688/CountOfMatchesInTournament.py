from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        if (n ^ 1) == (n + 1):
            return (n // 2) + self.numberOfMatches(n // 2)
        return ((n - 1) // 2) + self.numberOfMatches((n // 2) + 1)


# leetcode submit region end(Prohibit modification and deletion)


class CountOfMatchesInTournament(Solution):
    pass
