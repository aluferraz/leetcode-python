import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        """
        :type nums: List[int]
        :type modulo: int
        :type k: int
        :rtype: int
        """
        N = len(nums)
        m = modulo
        prefix = 0
        ans = 0
        counter = collections.defaultdict(int)
        counter[0] = 1

        for i in range(N):
            if nums[i] % m == k:
                prefix += 1
            prefix %= m
            target = (prefix - k + m) % m
            ans += (counter[target])
            counter[prefix] += 1
        return ans

        # leetcode submit region end(Prohibit modification and deletion)


class CountOfInterestingSubarrays(Solution):
    pass
