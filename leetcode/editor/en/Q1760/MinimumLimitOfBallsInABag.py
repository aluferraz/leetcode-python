from typing import List


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def ok(v):
            ops = 0
            for val in nums:
                ops += val // v
                if not (val % v):
                    ops -= 1
                if ops > maxOperations:
                    return False
            return True

        lo, hi = 1, 10 ** 9 + 5
        while lo <= hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        return lo

    # leetcode submit region end(Prohibit modification and deletion)


class MinimumLimitOfBallsInABag(Solution):
    pass
