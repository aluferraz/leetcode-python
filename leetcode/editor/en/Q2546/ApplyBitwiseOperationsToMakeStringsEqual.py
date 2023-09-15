from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def makeStringsEqual(self, s, t):

        N = len(s)
        ones_that_needs_to_be_zero = 0
        zeros_that_needs_to_be_one = 0

        ones = 0
        zeros = 0

        for i in range(N):
            if s[i] == "0":
                zeros += 1
                if s[i] == t[i]:
                    continue
                zeros_that_needs_to_be_one += 1
                # zeros_that_needs_to_be_one.add(i)
            else:
                ones += 1
                if s[i] == t[i]:
                    continue
                ones_that_needs_to_be_zero += 1
                # ones_that_needs_to_be_zero.add(i)

        @cache
        def go(o, z, zeros_that_needs_to_be_one, ones_that_needs_to_be_zero):
            if zeros_that_needs_to_be_one == 0 and \
                    ones_that_needs_to_be_zero == 0:
                return True
            ans = False
            if zeros_that_needs_to_be_one > 0:
                if ones_that_needs_to_be_zero > 1:
                    ans = go(o, z, zeros_that_needs_to_be_one - 1, ones_that_needs_to_be_zero - 1)
                    if ans:
                        return True
                if o > 0:
                    ans = go(o, z - 1, zeros_that_needs_to_be_one - 1, ones_that_needs_to_be_zero)
                    if ans:
                        return True
                else:
                    return False
            if ones_that_needs_to_be_zero > 0:
                if o > 1:
                    ans = go(o - 1, z, zeros_that_needs_to_be_one, ones_that_needs_to_be_zero - 1)
                    if ans:
                        return ans
                if zeros_that_needs_to_be_one > 0:
                    ans = go(o, z, ones_that_needs_to_be_zero - 1, zeros_that_needs_to_be_one - 1)

            return ans

        return go(ones, zeros, zeros_that_needs_to_be_one, ones_that_needs_to_be_zero)
        # TLE:
        #
        # def go(i, o, z):
        #     if i == N:
        #         return len(zeros_that_needs_to_be_one) == 0 and \
        #             len(ones_that_needs_to_be_zero) == 0
        #     # Simultaneously, replace s[i] with (s[i] OR s[j]) and s[j] with (s[i] XOR s[j]).
        #     if i in zeros_that_needs_to_be_one:
        #         if len(ones_that_needs_to_be_zero) > 1:
        #             # we can make this zero as one:
        #             # 0 or 1 -> 1
        #             # 0 ^ 1 -> 1
        #             # then we can make the one as zero:
        #             # 1 or 1 -> still 1
        #             # 1 ^ 1 -> 0
        #             make_one_zero = ones_that_needs_to_be_zero.pop()
        #             zeros_that_needs_to_be_one.remove(i)
        #             go(i + 1, o, z)
        #
        #
        #         elif o > 0:
        #             # i =  0 or 1 -> 1 .
        #             # j =  0 ^ 1 -> 1
        #             zeros_that_needs_to_be_one.remove(i)
        #             return go(i + 1, o, z - 1)
        #         else:
        #             return False
        #     if i in ones_that_needs_to_be_zero:
        #         # i =  1 or 1 -> 1 .
        #         # j =  1 ^ 1 -> 0
        #         if o > 1:
        #             ones_that_needs_to_be_zero.discard(i)
        #             return go(i + 1, o - 1, z)
        #         elif len(zeros_that_needs_to_be_one) > 0:
        #             # i = 1 or 0 -> 1
        #             # j = 1 ^ 0 -> 1
        #             make_zero_one = zeros_that_needs_to_be_one.pop()
        #             # use the new one to make this zero:
        #             # i =  1 or 1 -> 1 .
        #             # j =  1 ^ 1 -> 0
        #             ones_that_needs_to_be_zero.discard(i)
        #             return go(i + 1, o, z)
        #         else:
        #             return False
        #     return go(i + 1, o, z)


# leetcode submit region end(Prohibit modification and deletion)


class ApplyBitwiseOperationsToMakeStringsEqual(Solution):
    pass
