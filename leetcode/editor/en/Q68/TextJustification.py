import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        lines = []

        current_line = []
        llen = 0
        wlen = 0
        for w in words:
            if llen + len(w) <= maxWidth:
                current_line.append(w)
                llen += len(w) + 1
                wlen += len(w)
            else:
                lines.append((current_line, wlen))
                current_line = [w]
                llen = len(w) + 1
                wlen = len(w)
        if len(current_line) > 0:
            lines.append((current_line, wlen))

        ans = []
        N = len(lines)

        def go(i):
            words_arr, wlen = lines[i]
            text_line = []
            if i == N - 1:
                space_remaining = maxWidth - (wlen + len(words_arr) - 1)
                text_line.append(" ".join(words_arr))
                leading_spaces = [" "] * space_remaining
                text_line.append("".join(leading_spaces))
                ans.append("".join(text_line))
                return
            else:
                space_remaining = maxWidth - wlen
                if len(words_arr) > 1:
                    space_groups = [0] * (len(words_arr) - 1)
                    space_group_idx = 0
                    while space_remaining > 0:
                        space_groups[space_group_idx] += 1
                        space_group_idx += 1
                        space_group_idx %= len(space_groups)
                        space_remaining -= 1
                else:
                    space_groups = [space_remaining]
                space_groups = collections.deque(space_groups)

                for w in words_arr:
                    text_line.append(w)
                    if len(space_groups) > 0:
                        leading_spaces = [" "] * space_groups.popleft()
                        text_line.append("".join(leading_spaces))
                ans.append("".join(text_line))
                go(i + 1)

        go(0)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class TextJustification(Solution):
    pass
