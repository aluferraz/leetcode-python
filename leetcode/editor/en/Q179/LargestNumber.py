from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return "0" if sum(nums) == 0 else "".join(sorted([str(i) for i in nums], key=lambda x: x * 10, reverse=True))


# leetcode submit region end(Prohibit modification and deletion)


class LargestNumber(Solution):
    pass
