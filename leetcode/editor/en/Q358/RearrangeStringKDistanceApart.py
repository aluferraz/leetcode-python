import collections
from typing import List

import sortedcontainers


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return s
        counter = [0] * 26
        for c in s:
            counter[ord(c) - ord('a')] += 1
        chars = sortedcontainers.SortedList()
        for i in range(26):
            if counter[i] == 0:
                continue
            chars.add((-counter[i], i, chr(i + ord('a'))))

        N = len(s)
        can_use = [True] * 26
        ans = []
        ans_str = []
        pos = 0
        while len(ans) < N:
            if pos - k >= 0:
                can_use[ans[pos - k]] = True
            impossible = True
            for i in range(len(chars)):
                (cnt, asc, ch) = chars[i]

                if can_use[asc]:
                    chars.remove((cnt, asc, ch))
                    cnt = abs(cnt) - 1
                    can_use[asc] = False
                    ans.append(asc)
                    ans_str.append(ch)
                    pos += 1
                    impossible = False
                    if cnt > 0:
                        chars.add((-cnt, asc, ch))
                    break
            if impossible:
                return ""
        return "".join(ans_str)


# leetcode submit region end(Prohibit modification and deletion)


class RearrangeStringKDistanceApart(Solution):
    pass
