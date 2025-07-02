from sortedcontainers import SortedList


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def clearStars(self, s: str) -> str:
        letters = SortedList()
        N = len(s)
        for i in range(N):
            c = s[i]
            if c == '*':
                if letters:
                    letters.pop(0)
            else:
                letters.add((c, -i))
        sorted_ans = SortedList()
        for c, i in letters:
            sorted_ans.add((-i, c))
        return "".join([c for _, c in sorted_ans])


# leetcode submit region end(Prohibit modification and deletion)


class LexicographicallyMinimumStringAfterRemovingStars(Solution):
    pass
