from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        N = len(envelopes)

        cache = [None] * N

        def bin_search(left, right, dimension, target):
            ans = right
            while left <= right:
                mid = (left + right) // 2
                if envelopes[mid][dimension] < target:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        def go(i):
            if i == N:
                return 0
            if cache[i] is not None:
                return cache[i]
            cache[i] = 1
            start_height_idx = bin_search(0, i, 1, envelopes[i][1])
            if start_height_idx < i:
                cache[i] = max(cache[i], 1 + go(start_height_idx))

            return max(cache[i], go(i + 1))

        return go(0)


# leetcode submit region end(Prohibit modification and deletion)


class RussianDollEnvelopes(Solution):
    pass
