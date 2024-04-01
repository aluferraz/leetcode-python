from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        arr = []
        curr = []
        for n in nums:
            if n < minK or n > maxK:
                if len(curr) > 0:
                    arr.append(curr)
                    curr = []
            else:
                curr.append(n)
        if len(curr) > 0:
            arr.append(curr)
        def count_good(slice):
            last_max_idx = None
            last_min_idx = None
            total = 0
            for i in range(len(slice)):
                if slice[i] == minK:
                    last_min_idx = i
                if slice[i] == maxK:
                    last_max_idx = i
                if last_min_idx is not None and last_max_idx is not None:
                    total += min(last_max_idx, last_min_idx) + 1
            return total

        ans = 0
        for slice in arr:
            ans += count_good(slice)
        return ans

# leetcode submit region end(Prohibit modification and deletion)


class CountSubarraysWithFixedBounds(Solution):
    pass
