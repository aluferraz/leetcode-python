import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """

        counter = collections.Counter()

        def digit_sum(n):
            ans = 0
            if n > 0:
                return n % 10 + digit_sum(n // 10)
            return ans

        for i in range(lowLimit, highLimit + 1):
            box = digit_sum(i)
            counter[box] += 1
        return counter.most_common()[0][1]

# leetcode submit region end(Prohibit modification and deletion)


class MaximumNumberOfBallsInABox(Solution):
    pass
