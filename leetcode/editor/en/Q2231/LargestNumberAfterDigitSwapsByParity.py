import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        even = []
        odd = []
        numStr = str(num)
        N = len(numStr)
        for i in range(N):
            if int(numStr[i]) % 2 == 0:
                even.append(int(numStr[i]))
            else:
                odd.append(int(numStr[i]))
        even.sort()
        odd.sort()
        ans = 0

        for i in range(N):
            if int(numStr[i]) % 2 == 0:
                ans += ((10 ** (N - i - 1)) * even.pop())
            else:
                ans += ((10 ** (N - i - 1)) * odd.pop())

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class LargestNumberAfterDigitSwapsByParity(Solution):
    pass
