from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        letters = [0] * 26
        for c in chars:
            letters[ord(c) - ord('a')] += 1

        N = len(words)

        def go(i):
            if i == N:
                return 0
            can_build = True
            ans = 0
            for c in words[i]:
                letters[ord(c) - ord('a')] -= 1
                if letters[ord(c) - ord('a')] < 0:
                    can_build = False
            if can_build:
                ans = len(words[i])
            for c in words[i]:
                letters[ord(c) - ord('a')] += 1
            return ans + go(i + 1)

        return go(0)


# leetcode submit region end(Prohibit modification and deletion)


class FindWordsThatCanBeFormedByCharacters(Solution):
    pass
