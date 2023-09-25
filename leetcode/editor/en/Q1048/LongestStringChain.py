import collections
from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=lambda x: (len(x), x))
        N = len(words)
        ans = min(1, N)
        chain = 1

        def is_subsequence(a, b, i, j):
            if i == len(a):
                return True
            if j == len(b):
                return False
            if a[i] == b[j]:
                return is_subsequence(a, b, i + 1, j + 1)
            return is_subsequence(a, b, i, j + 1)

        words_by_len = [[] for _ in range(18)]

        for i in range(N):
            w = words[i]
            words_by_len[len(w)].append(i)

        ans = 1
        cache = [0] * N
        has_cache = [False] * N

        def get_best(i):
            if has_cache[i]:
                return cache[i]
            current_len = len(words[i])
            ans = 1
            for j in words_by_len[current_len + 1]:
                if is_subsequence(words[i], words[j], 0, 0):
                    ans = max(ans, 1 + get_best(j))
            has_cache[i] = True
            cache[i] = ans
            return ans

        for i in range(N):
            ans = max(ans, get_best(i))

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class LongestStringChain(Solution):
    pass
