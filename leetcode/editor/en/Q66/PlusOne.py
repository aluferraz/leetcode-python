import collections
import math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        q = collections.deque()

        carry = 1
        while len(digits) > 0 and carry == 1:
            nextDigit = digits.pop()
            nextDigit += 1
            if nextDigit == 10:
                carry = 1
                q.appendleft(0)
            else:
                carry = 0
                q.appendleft(nextDigit)
        if carry > 0:
            q.appendleft(carry)
        while len(digits) > 0:
            q.appendleft(digits.pop())

        return list(q)

    # leetcode submit region end(Prohibit modification and deletion)


class PlusOne(Solution):
    pass
