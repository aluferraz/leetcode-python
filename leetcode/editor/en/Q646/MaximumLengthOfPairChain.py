from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort()
        N = len(pairs)

        def bin_search(threshold):
            left = 0
            right = N
            while left < right:
                mid = (left + right) // 2
                if pairs[mid][0] > threshold:
                    right = mid
                else:
                    left = mid + 1
            return left

        cache = [None] * N

        def go(i):
            if i >= N:
                return 0
            if cache[i] is not None:
                return cache[i]
            s, e = pairs[i]
            next_idx = bin_search(e)
            use = 1 + go(next_idx)
            skip = go(i + 1)
            ans = max(use, skip)
            cache[i] = ans
            return ans

        return go(0)


# leetcode submit region end(Prohibit modification and deletion)


class MaximumLengthOfPairChain(Solution):
    pass
