from functools import cache
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxLength(self, arr: List[str]) -> int:

        N = len(arr)
        ans = 0
        @cache
        def go(i, used, word):
            if i == N:
                nonlocal ans
                ans = max(ans, len(word))
                return
            mask = 0
            for ch in arr[i]:
                c = ord(ch) - ord('a')
                if used & (1 << c) != 0 or mask & (1 << c) != 0:
                    return go(i+1, used, word)
                mask |= (1 << c)
            go(i+1, used | mask, word + arr[i])
            go(i + 1, used, word)

        go(0,0,"")
        return ans

# leetcode submit region end(Prohibit modification and deletion)


class MaximumLengthOfAConcatenatedStringWithUniqueCharacters(Solution):
    pass