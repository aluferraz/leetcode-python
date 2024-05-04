from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        existing = set()
        max_found = 0
        nums.sort()
        for n in nums:
            if n < 0:
                existing.add(n)
            else:
                if -n in existing:
                    max_found = n
        return max_found


# leetcode submit region end(Prohibit modification and deletion)


class LargestPositiveIntegerThatExistsWithItsNegative(Solution):
    pass
