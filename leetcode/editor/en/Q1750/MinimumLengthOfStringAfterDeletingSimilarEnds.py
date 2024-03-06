import sys
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumLength(self, s: str) -> int:
        N = len(s)
        sys.setrecursionlimit(10 ** 6)

        def go(left, right):
            ans = right - left + 1
            if left > right:
                return 0
            if left == right:
                return ans
            if s[left] == s[right]:
                removal = s[left]
                while left <= right and s[left] == removal:
                    left += 1
                while right >= left and s[right] == removal:
                    right -= 1
                ans = min(ans, go(left,right))
            return ans
        return go(0, N-1)


# leetcode submit region end(Prohibit modification and deletion)


class MinimumLengthOfStringAfterDeletingSimilarEnds(Solution):
    pass