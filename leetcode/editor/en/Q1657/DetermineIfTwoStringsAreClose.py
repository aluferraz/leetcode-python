# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        N = len(word1)
        for i in range(N):
            cnt1[ord(word1[i]) - ord('a')] += 1
            cnt2[ord(word2[i]) - ord('a')] += 1
        for i in range(26):
            if (cnt1[i] == 0 and cnt2[i] > 0) or \
                    (cnt2[i] == 0 and cnt1[i] > 0):
                return False

        cnt1.sort()
        cnt2.sort()
        for i in range(26):
            if cnt1[i] != cnt2[i]:
                return False

        return True







# leetcode submit region end(Prohibit modification and deletion)


class DetermineIfTwoStringsAreClose(Solution):
    pass
