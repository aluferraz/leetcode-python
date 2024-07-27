from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        new_nums = []
        nums_str = [str(x) for x in nums]
        for num in nums_str:
            new_str = []
            for c in num:
                new_str.append(str(mapping[int(c)]))
            new_nums.append("".join(new_str))
        new_nums = [int(x) for x in new_nums]

        sorted_nums = []
        N = len(new_nums)
        for i in range(N):
            sorted_nums.append((new_nums[i], i, nums[i]))
        sorted_nums.sort()
        return [x[2] for x in sorted_nums]


# leetcode submit region end(Prohibit modification and deletion)


class SortTheJumbledNumbers(Solution):
    pass
