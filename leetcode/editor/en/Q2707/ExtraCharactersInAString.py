# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """

        N = len(s)
        has_cache = [False for _ in range(N)]
        cache = [None for _ in range(N)]

        def count(i):
            if i == N:
                return 0
            if has_cache[i]:
                return cache[i]
            ans = N - i
            for word in dictionary:
                index = s.find(word, i, N)
                if index != -1:
                    cost = (index - i) + count(index + len(word))
                    ans = min(ans, cost)

            has_cache[i] = True
            cache[i] = ans
            return ans

        return count(0)


# leetcode submit region end(Prohibit modification and deletion)


class ExtraCharactersInAString(Solution):
    pass
