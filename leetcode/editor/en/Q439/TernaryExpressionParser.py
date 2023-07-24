import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        N = len(expression)
        if len(expression) == 1:
            return expression

        ans = collections.deque()
        for i in range(N - 1, -1, -1):
            ans.appendleft(expression[i])
            if len(ans) > 1 and ans[1] == '?':
                replace_with = ''
                if ans[0] == 'T':
                    replace_with = ans[2]
                else:
                    replace_with = ans[4]
                for _ in range(5):
                    ans.popleft()
                ans.appendleft(replace_with)
        return ans[0]


# leetcode submit region end(Prohibit modification and deletion)


class TernaryExpressionParser(Solution):
    pass
