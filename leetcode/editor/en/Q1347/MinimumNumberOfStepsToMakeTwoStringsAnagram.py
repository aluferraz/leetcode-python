import collections
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSteps(self, s: str, t: str) -> int:

        t = collections.Counter(t)
        N = len(s)
        def go(i):
            if i == N:
                return sum(t.values())
            c = s[i]
            if t[c] > 0:
                t[c] -= 1
                return go(i+1)
            return go(i+1)

        return go(0)
# leetcode submit region end(Prohibit modification and deletion)


class MinimumNumberOfStepsToMakeTwoStringsAnagram(Solution):
    pass