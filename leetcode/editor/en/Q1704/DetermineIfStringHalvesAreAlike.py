import collections
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        N = len(s)
        cnt = 0
        targets = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for i in range(N//2):
            if s[i] in targets:
                cnt += 1

        for i in range(N // 2, N):
            if s[i] in targets:
                cnt -= 1

        return cnt == 0
# leetcode submit region end(Prohibit modification and deletion)


class DetermineIfStringHalvesAreAlike(Solution):
    pass