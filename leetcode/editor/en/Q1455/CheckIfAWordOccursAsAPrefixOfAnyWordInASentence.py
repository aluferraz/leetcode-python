# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        N = len(words)
        for i in range(N):
            if words[i].startswith(searchWord):
                return i + 1
        return -1


# leetcode submit region end(Prohibit modification and deletion)


class CheckIfAWordOccursAsAPrefixOfAnyWordInASentence(Solution):
    pass
