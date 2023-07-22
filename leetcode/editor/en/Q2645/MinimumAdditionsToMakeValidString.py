from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def addMinimum(self, word):
        """
        :type word: str
        :rtype: int
        """
        N = len(word)

        def go(i, target):
            if i == N and target == 'a':
                return 0

            if target == 'a':
                next_target = 'b'
            if target == 'b':
                next_target = 'c'
            if target == 'c':
                next_target = 'a'
            current = word[i] if i < N else ''
            if current == target:
                return go(i + 1, next_target)
            else:
                return 1 + go(i, next_target)

        return go(0, 'a')


# leetcode submit region end(Prohibit modification and deletion)


class MinimumAdditionsToMakeValidString(Solution):
    pass
