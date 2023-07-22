import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        N = len(asteroids)
        ans = []

        for ast in asteroids:
            ans.append(ast)
            while len(ans) >= 2 and ans[-2] > 0 and ans[-1] < 0:
                if abs(ans[-2]) == abs(ans[-1]):
                    ans.pop()
                    ans.pop()
                elif abs(ans[-2]) > abs(ans[-1]):
                    ans.pop()
                else:
                    remaining = ans.pop()
                    ans.pop()
                    ans.append(remaining)

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class AsteroidCollision(Solution):
    pass
