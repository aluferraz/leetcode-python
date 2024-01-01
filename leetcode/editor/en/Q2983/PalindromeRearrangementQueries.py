import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canMakePalindromeQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        N = len(s)
        counter_l = collections.defaultdict(list)
        counter_r = collections.defaultdict(list)

        counter = [0] * 26
        for i in range(N // 2):
            counter_l[(0, i)] = list(counter)
            counter[ord(s[i]) - ord('a')] += 1
            counter_l[(0, i)][ord(s[i]) - ord('a')] += 1
        counter = [0] * 26
        for i in range(N // 2, N):
            counter_r[(N // 2, i)] = list(counter)
            counter[ord(s[i]) - ord('a')] += 1
            counter_r[(N // 2, i)][ord(s[i]) - ord('a')] += 1
        ans = [False] * len(queries)

        def sub_arr(a1, a2):
            ans = a2
            for i in range(26):
                ans[i] -= a1[i]
            return ans

        def get_count(l, r, s, arr):
            rcount = arr[(s, r)]
            if l == s:
                return rcount
            lcount = arr[(s, l - 1)]
            return sub_arr(lcount, rcount)

        for q in range(len(queries)):
            ll, lr, rl, rr = queries[q]
            charsl = get_count(ll, lr, 0, counter_l)
            charsr = get_count(rl, rr, N // 2, counter_r)
            diff = sub_arr(charsl, charsr)
            ans[q] = min(diff) >= 0

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class PalindromeRearrangementQueries(Solution):
    pass
