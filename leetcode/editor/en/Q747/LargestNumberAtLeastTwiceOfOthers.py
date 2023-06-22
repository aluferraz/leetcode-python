from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        numsNew = [(nums[i], i) for i in range(N)]
        numsNew.sort()
        ans = -1
        if numsNew[-1][0] >= numsNew[-2][0] * 2:
            ans = numsNew[-1][1]
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class LargestNumberAtLeastTwiceOfOthers(Solution):
    pass
