import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = collections.Counter()
        left = 0
        right = 0
        N = len(nums)
        ans = 0
        while right < N:
            cnt[nums[right]] += 1
            while left <= right and cnt[nums[right]] > 1:
                ans += 1
                for _ in range(3):
                    if left == N:
                        break
                    cnt[nums[left]] -= 1
                    left += 1
            right += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MinimumNumberOfOperationsToMakeElementsInArrayDistinct(Solution):
    pass
