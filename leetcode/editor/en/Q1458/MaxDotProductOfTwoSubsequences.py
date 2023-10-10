from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # N = len(nums1)
        # M = len(nums2)
        # INF = 10 ** 20

        # has_cache = [[False for _ in range(M)] for _ in range(N)]
        # cache = [[0 for _ in range(M)] for _ in range(N)]
        #
        # def go(starti, startj):
        #     if starti == N or startj == M:
        #         return 0
        #     if has_cache[starti][startj]:
        #         return cache[starti][startj]
        #     best = 0 if starti > 0 else -INF
        #
        #     for i in range(N - 1, starti - 1, -1):
        #         for j in range(M - 1, startj - 1, -1):
        #             best = max(best,
        #                        (nums1[i] * nums2[j]) +
        #
        #                        go(i + 1, j + 1)
        #                        )
        #     has_cache[starti][startj] = True
        #     cache[starti][startj] = best
        #     return best
        #
        # return go(0, 0)
        N, M = len(nums1), len(nums2)
        INF = 10 ** 20
        # Initialize the cache with base values.
        cache = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

        # Iterate from the end of the lists towards the beginning.
        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                # The current value is the product of the current elements
                # plus the value from the next step.
                cache[i][j] = max(
                    nums1[i] * nums2[j] + cache[i + 1][j + 1],
                    cache[i + 1][j],  # Skip the current element of nums1
                    cache[i][j + 1]  # Skip the current element of nums2
                )
        if cache[0][0] == 0:
            best = -INF
            for i in range(N):
                for j in range(M):
                    best = max(best, nums1[i] * nums2[j])
            return best
        return cache[0][0]

# leetcode submit region end(Prohibit modification and deletion)


class MaxDotProductOfTwoSubsequences(Solution):
    pass
