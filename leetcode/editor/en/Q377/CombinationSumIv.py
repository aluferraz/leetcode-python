from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        N = len(nums)

        has_cache = [False] * (target + 1)
        cache = [0] * (target + 1)

        def go(target):
            if target == 0:
                return 1
            if has_cache[target]:
                return cache[target]
            ans = 0
            for n in nums:
                if n > target:
                    break
                ans += go(target - n)
            has_cache[target] = True
            cache[target] = ans
            return ans

        return go(target)


# leetcode submit region end(Prohibit modification and deletion)


class CombinationSumIv(Solution):
    pass
