from functools import cache
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkValidString(self, s: str) -> bool:
        N = len(s)
        @cache
        def is_valid(i,open):
            if i == N:
                return open == 0
            if open < 0:
                return False
            if s[i] == '(':
                return is_valid(i+1, open + 1)
            if s[i] == ')':
                return is_valid(i + 1, open - 1)
            #it's *
            return is_valid(i + 1, open - 1) or \
                    is_valid(i + 1, open + 1) or \
                    is_valid(i + 1, open)
        return is_valid(0,0)

# leetcode submit region end(Prohibit modification and deletion)


class ValidParenthesisString(Solution):
    pass