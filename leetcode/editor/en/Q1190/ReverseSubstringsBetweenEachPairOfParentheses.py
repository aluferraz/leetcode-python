# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def reverseParentheses(self, s: str) -> str:

        N = len(s)
        open = []
        cur = []
        for i in range(N):
            c = s[i]
            if c == '(':
                open.append(i)
            if c == ')':
                should_reverse = (i - open.pop())
                rev = collections.deque()
                for _ in range(should_reverse):
                    rev.append(cur.pop())
                for _ in range(should_reverse):
                    cur.append(rev.popleft())
            cur.append(s[i])
        ans = "".join(cur)
        ans = ans.replace("(", "")
        ans = ans.replace(")", "")

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class ReverseSubstringsBetweenEachPairOfParentheses(Solution):
    pass
