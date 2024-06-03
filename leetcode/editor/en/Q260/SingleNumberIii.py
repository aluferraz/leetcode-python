from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c = 0
        N = len(nums)
        for i in range(N):
            c ^= nums[i]
        # c = a ^ b
        # only a or b can have a bit as 1
        pos = 0
        for i in range(64):
            if ((1 << i) & c) != 0:
                pos = i
                break
        b = 0
        for n in nums:
            if ((1 << pos) & n) != 0:
                # Other numbers can have 1 in this position but they will cancel out.
                b ^= n
        return [c ^ b, b]


# leetcode submit region end(Prohibit modification and deletion)


class SingleNumberIii(Solution):
    pass
