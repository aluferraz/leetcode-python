from collections import defaultdict
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        l1, l2 = len(nums1), len(nums2)
        f = defaultdict(int)

        for i in nums1:
            f[i] += l2
        for i in nums2:
            f[i] += l1

        for i in f:
            if f[i] % 2 != 0:
                ans = ans ^ i
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class BitwiseXorOfAllPairings(Solution):
    pass
