from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        ans = 0

        arr = text.split(" ")

        bk = set(brokenLetters)

        for w in arr:
            for l in w:
                if l in bk:
                    ans += 1
                    break
        return len(arr) - ans


# leetcode submit region end(Prohibit modification and deletion)


class MaximumNumberOfWordsYouCanType(Solution):
    pass
