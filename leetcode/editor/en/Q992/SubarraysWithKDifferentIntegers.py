import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarray_with_most(arr, limit):
            if limit == 0:
                return 0
            left = 0
            right = 0
            seen = collections.defaultdict(int)
            N = len(arr)
            total = 0
            while right < N:
                seen[arr[right]] += 1
                while len(seen.keys()) > limit:
                    seen[arr[left]] -= 1
                    if seen[arr[left]] == 0:
                        seen.pop(arr[left])
                    left += 1
                total += right - left + 1
                right += 1
            return total

        return subarray_with_most(nums, k) - subarray_with_most(nums, k - 1)


# leetcode submit region end(Prohibit modification and deletion)


class SubarraysWithKDifferentIntegers(Solution):
    pass
