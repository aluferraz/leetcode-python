from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()

        ans = []
        current = []
        for n in nums:
            if len(current) == 0 or n - current[0] <= k:
                current.append(n)
                if len(current) == 3:
                    ans.append(current)
                    current = []
            else:
                return []

        return ans if len(current) == 0 else []






# leetcode submit region end(Prohibit modification and deletion)


class DivideArrayIntoArraysWithMaxDifference(Solution):
    pass