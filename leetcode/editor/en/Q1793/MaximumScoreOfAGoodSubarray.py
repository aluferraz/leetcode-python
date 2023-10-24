import collections
import heapq
from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)

class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        INF = 10 ** 20
        N = len(nums)
        numbers = []
        for i in range(N):
            numbers.append((nums[i], i))
        heapq.heapify(numbers)
        ans = 0
        i = 0
        j = N - 1
        while len(numbers) > 0:
            if i > k or j < k:
                return ans
            while numbers[0][1] < i or numbers[0][1] > j:
                heapq.heappop(numbers)
                if len(numbers) == 0:
                    return ans
            ans_here = (numbers[0][0] * ((j - i) + 1))
            ans = max(ans, ans_here)
            _, shrink = heapq.heappop(numbers)
            if shrink < k:
                i = max(i, shrink + 1)
            elif shrink > k:
                j = min(j, shrink - 1)
            else:
                ans = max(ans, nums[k])
                return ans

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MaximumScoreOfAGoodSubarray(Solution):
    pass
