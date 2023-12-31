import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        N = len(words)

        count = collections.Counter()
        for w in words:
            for c in w:
                count[c] += 1

        for v in count.values():
            if v % N != 0:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)


class RedistributeCharactersToMakeAllStringsEqual(Solution):
    pass
