from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nlist = list(sorted(set(nums)))
        if nlist[0] < k:
            return -1
        if nlist[0] == k:
            return len(nlist) - 1
        return len(nlist)


# leetcode submit region end(Prohibit modification and deletion)


class MinimumOperationsToMakeArrayValuesEqualToK(Solution):
    pass
