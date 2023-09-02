from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)

        last_seen = -1
        seen_count = 0
        pos = 0
        for i in range(N):
            if nums[i] != last_seen:
                last_seen = nums[i]
                nums[pos] = nums[i]
                pos += 1
                seen_count = 1
                continue
            elif seen_count == 1:
                nums[pos] = nums[i]
                pos += 1
                seen_count += 1
            else:
                continue
        return pos

        # leetcode submit region end(Prohibit modification and deletion)


class RemoveDuplicatesFromSortedArrayIi(Solution):
    pass
