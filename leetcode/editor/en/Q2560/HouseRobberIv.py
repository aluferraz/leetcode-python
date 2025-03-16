from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        N = len(nums)
        INF = 10 ** 20

        def rob(i, limit):
            ans = 0
            if i >= N:
                return ans
            if nums[i] <= limit:
                return 1 + rob(i + 2, limit)
            return rob(i + 1, limit)

        def good(answer_candidate):
            return rob(0, answer_candidate) >= k

        left = 0
        right = 10 ** 9 + 1
        while left < right:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid + 1
        return left


# leetcode submit region end(Prohibit modification and deletion)


class HouseRobberIv(Solution):
    pass
