from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        N = len(nums)
        for i in range(1, N):
            for j in range(i, 0, -1):
                if nums[j - 1].bit_count() == nums[j].bit_count() and \
                        nums[j - 1] > nums[j]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
                else:
                    break
        return nums == sorted(nums)


# leetcode submit region end(Prohibit modification and deletion)


class FindIfArrayCanBeSorted(Solution):
    pass
