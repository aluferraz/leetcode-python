from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxDepth(self, s: str) -> int:
        open = []
        ans = 0
        for c in s:
            if c == '(':
                open.append(c)
            elif c == ')':
                if len(open) > 0:
                    ans = max(ans, len(open))
                    open.pop()
        return ans



# leetcode submit region end(Prohibit modification and deletion)


class MaximumNestingDepthOfTheParentheses(Solution):
    pass