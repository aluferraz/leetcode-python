import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = collections.Counter(s1.split(' '))
        s2 = collections.Counter(s2.split(' '))
        ans = []
        for w, cnt in s1.items():
            if cnt > 1:
                continue
            if w not in s2:
                ans.append(w)
        for w, cnt in s2.items():
            if cnt > 1:
                continue
            if w not in s1:
                ans.append(w)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class UncommonWordsFromTwoSentences(Solution):
    pass
