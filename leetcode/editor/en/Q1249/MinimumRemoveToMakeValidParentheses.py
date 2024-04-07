from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        N = len(s)
        open = []
        must_remove = set()
        for i in range(N):
            c = s[i]
            if c == '(':
                open.append(i)
            elif c == ')':
                if len(open) == 0:
                    must_remove.add(i)
                else:
                    open.pop()
        for remaining in open:
            must_remove.add(remaining)
        ans = []
        for i in range(N):
            if i in must_remove:
                continue
            ans.append(s[i])
        return "".join(ans)






# leetcode submit region end(Prohibit modification and deletion)


class MinimumRemoveToMakeValidParentheses(Solution):
    pass