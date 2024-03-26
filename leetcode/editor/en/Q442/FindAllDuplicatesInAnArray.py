from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mask = 0
        ans = []
        for n in nums:
            if (1 << n) & mask != 0:
                ans.append(n)
            mask |= (1 << n)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


class FindAllDuplicatesInAnArray(Solution):
    pass