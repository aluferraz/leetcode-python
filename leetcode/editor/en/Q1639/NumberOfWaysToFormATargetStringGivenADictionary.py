import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numWays(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        letters = {}

        for word in words:
            for i in range(len(word)):
                c = word[i]
                if (i not in letters):
                    letters[i] = [0 for _ in range(26)]
                letters[i][ord(c) - ord('a')] += 1
        N = len(target)
        cache = {}

        MOD = (10 ** 9) + 7

        def count(i, k):
            if i == N:
                return 1
            if k not in letters:
                return 0
            if (i, k) in cache:
                return cache[(i, k)]

            ans = 0
            needed = ord(target[i]) - ord('a')
            if letters[k][needed] == 0:
                cache[(i, k)] = count(i, k + 1)
                return cache[(i, k)]
            ways = letters[k][needed]

            ans = (ways * count(i + 1, k + 1)) % MOD
            ans = (ans + count(i, k + 1)) % MOD
            cache[(i, k)] = ans
            return ans

        return count(0, 0)


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfWaysToFormATargetStringGivenADictionary(Solution):
    pass
