import collections
from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumScore(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        N = len(s)
        M = len(t)

        letters_map = collections.defaultdict(list)
        for i in range(N):
            letters_map[s[i]].append(i)

        def bin_search(min_idx, arr):
            left = 0
            right = len(arr) - 1
            ans = N
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] >= min_idx:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans if ans == N else arr[ans]

        @cache
        def make_sub(i, j, k):
            if k < 0:
                return False
            if i == N:
                return j == M
            if j == M:
                return True

            ans = False
            target = t[j]
            arr = letters_map[target]
            if len(arr) == 0:
                return make_sub(i, j + 1, k - 1)
            next_i = bin_search(i+1, arr)
            if next_i == N:
                return make_sub(i, j + 1, k - 1)
            else:
                return make_sub(next_i, j + 1, k) or make_sub(i, j + 1, k - 1)

        def can_be_subsequence(k):
            return make_sub(-1, 0, k)

        left = 0
        right = M

        while left < right:
            mid = (left + right) // 2
            if can_be_subsequence(mid):
                right = mid
            else:
                left = mid + 1
        required_k = left
        INF = 10 ** 20
        ans = [INF, -INF]

        def get_score(i, j, k, min_idx, max_idx):
            nonlocal ans
            if k < 0:
                return False
            if i == N:
                if j == M:
                    ans = min(ans, [min_idx, max_idx])
                return j == M
            if j == M:
                ans = min(ans, [min_idx, max_idx])
                return True

            target = t[j]
            arr = letters_map[target]
            if len(arr) == 0:
                return get_score(i, j + 1, k - 1, min(min_idx, j), max(max_idx, j))
            next_i = bin_search(i + 1, arr)
            if next_i == N:
                return get_score(i, j + 1,
                                 k - 1,
                                 min(min_idx,
                                     j),
                                 max(max_idx,
                                     j))
            else:
                return get_score(next_i, j + 1, k, min_idx, max_idx) or get_score(i, j + 1,
                                                                                  k - 1,
                                                                                  min(min_idx,
                                                                                      j),
                                                                                  max(max_idx,
                                                                                      j))

        get_score(-1, 0, required_k, INF, -INF)
        return max(ans[1] - ans[0] + 1, 0)


# leetcode submit region end(Prohibit modification and deletion)


class SubsequenceWithTheMinimumScore(Solution):
    pass
