from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        ans = set()
        N = len(nums)
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    if (nums[j] - nums[i]) == diff == (nums[k] - nums[j]):
                        ans.add((i, j, k))
        return len(ans)


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfArithmeticTriplets(Solution):
    pass
