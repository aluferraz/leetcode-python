from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lastSeen1 = -1
        lastSeen2 = -1
        ans = 10 ** 20
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                lastSeen1 = i
            elif wordsDict[i] == word2:
                lastSeen2 = i

            if lastSeen1 >= 0 and lastSeen2 >= 0:
                ans = min(ans, abs(lastSeen2 - lastSeen1))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class ShortestWordDistance(Solution):
    pass
