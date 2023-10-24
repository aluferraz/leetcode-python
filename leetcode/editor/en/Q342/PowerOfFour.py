from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 4 == 0:
            n //= 4
        return n == 1
# leetcode submit region end(Prohibit modification and deletion)


class PowerOfFour(Solution):
    pass
    