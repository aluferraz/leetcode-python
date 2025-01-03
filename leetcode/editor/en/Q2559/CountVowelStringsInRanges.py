from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        N = len(words)
        good = [0] * N
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(N):
            if words[i][0] in vowels and \
                words[i][-1] in vowels:
                good[i] = 1
        presum = [0] * N
        presum[0] = good[0]
        for i in range(1, N):
            presum[i] = presum[i-1] + good[i]
        ans = []
        for l,r in queries:
            to_remove = presum[l-1] if l > 0 else 0
            ans.append(presum[r] - to_remove)
        return ans

# leetcode submit region end(Prohibit modification and deletion)


class CountVowelStringsInRanges(Solution):
    pass
    