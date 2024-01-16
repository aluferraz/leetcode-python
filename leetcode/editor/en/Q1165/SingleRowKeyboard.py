# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        N = len(word)
        indexes = [0] * 26
        for i in range(len(keyboard)):
            indexes[ord(keyboard[i]) - ord('a')] = i

        def go(i, pos):
            if i == N:
                return 0
            c = ord(word[i]) - ord('a')
            move = abs(pos - indexes[c])
            return move + go(i + 1, indexes[c])

        return go(0, 0)


# leetcode submit region end(Prohibit modification and deletion)


class SingleRowKeyboard(Solution):
    pass
