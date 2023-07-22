from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        N = len(nums)
        cache = [None for _ in range(N)]

        def go(i):
            if i == N:
                return (0, 0)
            if cache[i] is not None:
                return cache[i]

            best_here = 1
            best_here_cnt = 1
            for j in range(i + 1, N):
                if nums[j] > nums[i]:
                    use, cnt = go(j)
                    use += 1
                    if use > best_here:
                        best_here = use
                        best_here_cnt = cnt
                    elif use == best_here:
                        best_here_cnt += cnt
            ans = (best_here, best_here_cnt)
            # ans = max(ans, go(i + 1))
            cache[i] = ans
            return ans

        best_pair = (0, 0)
        for i in range(N):
            best_pair = max(best_pair, go(i))
        longest, longest_occurrence = best_pair
        ans = 0
        for l, c in cache:
            if l == longest:
                ans += c
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfLongestIncreasingSubsequence(Solution):
    pass
