from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = [0] * 101
        ans = 0
        for n in nums:
            cnt[n] += 1
        for i in range(101):
            if cnt[i] > 1:
                ans += (cnt[i] * (cnt[i] - 1)) // 2
        return ans
# leetcode submit region end(Prohibit modification and deletion)


class NumberOfGoodPairs(Solution):
    pass
