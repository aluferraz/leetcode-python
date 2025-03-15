import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        N = len(nums)
        seen = collections.defaultdict(set)
        good_pairs = 0

        def sum_natural_numbers(n):
            return n * (n + 1) // 2

        total_pairs = sum_natural_numbers(N - 1)
        for j in range(N):
            target = j
            if (nums[j] - target) in seen:
                new_target = j - (nums[j] - target)
                if new_target in seen[(nums[j] - target)]:
                    good_pairs += 1
            seen[nums[j]].add(j)

        return total_pairs - good_pairs


# leetcode submit region end(Prohibit modification and deletion)


class CountNumberOfBadPairs(Solution):
    pass
