import math
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
perfect_squares = set()


class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)

        def is_perfect_square(num):
            # Check if the number is equal to the integer square root squared
            sqrt_num = int(num ** 0.5)
            return sqrt_num * sqrt_num == num

        cache = [0] * (N + 1)
        has_cache = [False] * (N + 1)

        def find_pairs(last_index):
            if last_index > N:
                return 0
            if has_cache[last_index]:
                return cache[last_index]
            ans = 0


            for j in range(last_index + 1, N + 1):
                if is_perfect_square(last_index * j):
                    ans = max(ans, nums[last_index - 1] + nums[j - 1] + find_pairs(j))
            cache[last_index] = max(ans - nums[last_index - 1], 0)
            has_cache[last_index] = True
            return ans

        ans = 0
        # for i in range(1, N + 1):
        for i in range(N, 0, -1):
            ans_here = find_pairs(i)
            ans_here = max(ans_here, nums[i - 1])
            ans = max(ans, ans_here)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MaximumElementSumOfACompleteSubsetOfIndices(Solution):
    pass
