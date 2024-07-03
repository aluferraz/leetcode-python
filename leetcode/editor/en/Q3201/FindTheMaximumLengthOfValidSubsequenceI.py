from functools import cache
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        k = 2
        nums = [x % k for x in nums]
        N = len(nums)

        def go(i,acc, target_mod):
            if i >= N:
                return 0

            ans = 0
            if (nums[i] + acc) % k == target_mod:
                #append i to sequence and move on
                ans = 1 + go(i+1, nums[i] , target_mod)
            else:
                ans = go(i+1, acc,  target_mod)
            return ans
        ans = 0
        for i in range(0,N-1):
            ans = max(ans, 1 + go(i+1, nums[i], 0), 1 + go(i+1,nums[i],1))
        return ans




        
# leetcode submit region end(Prohibit modification and deletion)


class FindTheMaximumLengthOfValidSubsequenceI(Solution):
    pass
    