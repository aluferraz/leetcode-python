from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        ans = 0
        g.sort(reverse=True)
        s.sort()

        N = len(g)

        for i in range(N):
            if len(s) == 0:
                break
            if s[-1] < g[i]:
                continue
            ans += 1
            s.pop()
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class AssignCookies(Solution):
    pass
