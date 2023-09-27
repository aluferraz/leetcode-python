from _continuation import permute

import collections
import heapq
from typing import List

from itertools import permutations


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = collections.Counter(s)
        N = len(s)
        monostack = []
        seen = set()
        for c in s:
            if c not in seen:
                while len(monostack) > 0 and c <= monostack[-1] and cnt[monostack[-1]] > 0:
                    seen.discard(monostack.pop())
                monostack.append(c)
                seen.add(c)
                cnt[c] -= 1
        return "".join(monostack)


# leetcode submit region end(Prohibit modification and deletion)


class RemoveDuplicateLetters(Solution):
    pass
