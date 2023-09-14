from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def makeStringsEqual(self, s, t):
        pass
        # """
        # :type s: str
        # :type target: str
        # :rtype: bool
        # """
        #
        # zeros = s.count("0")
        # ones = s.count("1")
        # N = len(s)
        #
        # t_zeros = t.count("0")
        # t_ones = t.count("1")
        #
        # def can_make_ones(i, z, o):
        #     if i == N:
        #         return o >= t_ones
        #     if s[i] == t[i]:
        #         return can_make_ones(i + 1, z, o)
        #     sv = s[i]
        #     tv = t[i]
        #     if sv == "0" and tv == "1":
        #         if o == 0:
        #             return False
        #         return can_make_ones(i + 1, z - 1, o + 1)
        #     return can_make_ones(i + 1, z, o)
        #
        # def can_make_zeros(i, z, o):
        #     if i == N:
        #         if o == t_ones and z == t_zeros:
        #             return True
        #         if z > t_zeros and o < t_ones and o >= 1:
        #             return True
        #         return False
        #     if s[i] == t[i]:
        #         return can_make_zeros(i + 1, z, o)
        #     sv = s[i]
        #     tv = t[i]
        #     if sv == "1" and tv == "0":
        #         if o == 0:
        #             return False
        #         ans = False
        #         if o >= 1 and z > 0:
        #             # make 0 -> 1 using OR
        #             # make 11 -> 00 using XOR
        #             ans = can_make_zeros(i + 1, z + 1, o - 1)
        #         #
        #         if ans:
        #             return ans
        #     # make 11 -> 00
        #     return can_make_zeros(i + 1, z + 2, o - 2)
        #
        # ans = can_make_ones(0, zeros, ones)
        # if not ans:
        #     return False
        # s = list(s)
        # for i in range(N):
        #     if t[i] == "1" and s[i] == "0":
        #         s[i] = "1"
        #         zeros -= 1
        #         ones += 1
        #
        # return can_make_zeros(0, zeros, ones)


# leetcode submit region end(Prohibit modification and deletion)


class ApplyBitwiseOperationsToMakeStringsEqual(Solution):
    pass
