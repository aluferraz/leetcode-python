from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left = 1
        right = (position[-1] - position[0] + 1)
        N = len(position)

        def good(target):
            count = 0
            min_seen = position[0]
            for i in range(1, N):
                diff_here = position[i] - min_seen
                if diff_here >= target:
                    count += 1
                    min_seen = position[i]
            return count >= (m - 1)

        ans = 0
        while left < right:
            mid = (left + right) // 2
            if good(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MagneticForceBetweenTwoBalls(Solution):
    pass
