import collections
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def takeCharacters(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0


        def good(l,r,a,b,c, takes):
            if l > r:
                return (max(a, 0) + max(b, 0) + max(c, 0)) == 0
            if takes == 0:
                return (max(a,0) + max(b,0) + max(c,0)) == 0
            cleft = s[l]
            cright = s[r]
            ans = False
            if cleft == 'a':
                ans = good(l + 1, r, a-1,b,c, takes - 1)
            elif cleft == 'b':
                ans = good(l + 1, r, a,b-1,c, takes - 1)
            elif cleft == 'c':
                ans = good(l + 1, r, a,b,c-1, takes - 1)
            if not ans:
                if cright == 'a':
                    ans = good(l, r - 1, a - 1, b, c, takes - 1)
                elif cright == 'b':
                    ans = good(l, r - 1, a, b - 1, c, takes - 1)
                elif cright == 'c':
                    ans = good(l, r - 1, a, b, c - 1, takes - 1)
            return ans
        N = len(s)
        left = 0
        right = N + 1
        ans = -1
        while left < right:
            mid = (left + right) // 2
            if good(0, N-1,k,k,k, mid):
                ans = mid
                right = mid
            else:
                left = mid + 1
        return ans





# leetcode submit region end(Prohibit modification and deletion)


class TakeKOfEachCharacterFromLeftAndRight(Solution):
    pass
    