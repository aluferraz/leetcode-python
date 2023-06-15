from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countValidWords(self, sentence):
        """
        :type sentence: str
        :rtype: int
        """

        words = sentence.split(" ")
        ans = 0
        for word in words:
            N = len(word)
            hasHifen = False
            for i in range(N):
                if word[i].isnumeric():
                    break
                if word[i].isalpha():
                    if i == N - 1:
                        ans += 1
                    continue
                if word[i] == '-':
                    if i == 0 or i == N - 1 or hasHifen or (not word[i - 1].isalpha()) or (not word[i + 1].isalpha()):
                        break
                    else:
                        hasHifen = True
                else:
                    if i == N - 1:
                        ans += 1
                    else:
                        break
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfValidWordsInASentence(Solution):
    pass
