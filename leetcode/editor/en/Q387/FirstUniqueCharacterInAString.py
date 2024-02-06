import collections
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = collections.Counter(s)
        for i in range(len(s)):
            if cnt[s[i]] == 1:
                return i
        return -1
# leetcode submit region end(Prohibit modification and deletion)


class FirstUniqueCharacterInAString(Solution):
    pass