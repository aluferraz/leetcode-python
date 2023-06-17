from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        N = len(rods)
        cache = {}

        def findCorresp(i, sum, mask, target):
            if sum == target:
                return target
            if i == N or sum > target or rods[i] > target:
                return 0
            if (target, mask) in cache:
                return cache[(target, mask)]
            ans = 0
            if mask & (1 << (i + 1)) == 0:
                use = findCorresp(i + 1, sum + rods[i], mask | (1 << (i + 1)), target)
                skip = findCorresp(i + 1, sum, mask, target)
                ans = max(use, skip)
            else:
                ans = findCorresp(i + 1, sum, mask, target)
            cache[(target, mask)] = ans
            return ans

        cache2 = {}

        def find(i, sum, mask):
            ans = 0
            if i == N:
                return ans
            if (sum, mask) in cache2:
                return cache2[(sum, mask)]

            ans = findCorresp(0, 0, mask | (1 << (i + 1)), sum + rods[i])
            use = find(i + 1, sum + rods[i], mask | (1 << (i + 1)))
            skip = find(i + 1, sum, mask)
            ans = max(ans, use, skip)
            cache2[(sum, mask)] = ans
            return ans

        rods.sort()

        return find(0, 0, 0)
        # leetcode submit region end(Prohibit modification and deletion)


class TallestBillboard(Solution):
    pass
