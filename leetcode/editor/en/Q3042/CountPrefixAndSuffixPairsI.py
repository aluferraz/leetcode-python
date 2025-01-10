from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        N = len(words)
        for i in range(N):
            for j in range(i + 1, N):
                if len(words[j]) >= len(words[i]) and \
                        words[j][:len(words[i])] == words[i] and \
                        words[j][-(len(words[i]))::] == words[i]:
                    ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class CountPrefixAndSuffixPairsI(Solution):
    pass
