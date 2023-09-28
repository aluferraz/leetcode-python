import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def decodeAtIndex(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        N = len(s)
        word = []
        shifting = 0
        for i in range(N):
            c = s[i]
            if c.isdigit():
                for j in len(word):
                    if k % ((j*1) * int(c)) == 0:
                        return

            else:
                # last_occurrence[c] = real_pos
                real_pos += 1
                if real_pos == k:
                    return c
                word.append((c, real_pos))

        return ""


# leetcode submit region end(Prohibit modification and deletion)


class DecodedStringAtIndex(Solution):
    pass
