import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        ans = collections.deque()
        columnNumber -= 1
        c = 1
        while columnNumber >= pow(26, c):
            columnNumber -= pow(26, c)
            c += 1

        for _ in range(c):
            ans.appendleft(chr((columnNumber % 26) + ord('A')))
            columnNumber //= 26

        return "".join(ans)


# leetcode submit region end(Prohibit modification and deletion)


class ExcelSheetColumnTitle(Solution):
    pass
