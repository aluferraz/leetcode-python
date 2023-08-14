from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def validPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)

        cache = [None] * N

        def go(i):
            if i >= N:
                return True
            if cache[i] is not None:
                return cache[i]
            ans = False
            if i + 1 < N and nums[i] == nums[i + 1]:
                ans = go(i + 2)
                if not ans:
                    if i + 2 < N and nums[i] == nums[i + 2]:
                        ans = go(i + 3)
            if not ans:
                if i + 2 < N and nums[i] == nums[i + 1] - 1 and nums[i + 1] == nums[i + 2] - 1:
                    ans = go(i + 3)
            cache[i] = ans
            return ans

        return go(0)

        # leetcode submit region end(Prohibit modification and deletion)


class CheckIfThereIsAValidPartitionForTheArray(Solution):
    pass
