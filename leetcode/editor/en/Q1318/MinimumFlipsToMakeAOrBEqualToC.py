# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        abin = format(a, "#0b")[2:]
        bbin = format(b, "#0b")[2:]
        cbin = format(c, "#0b")[2:]
        N = max(len(cbin), len(abin), len(bbin))

        def lpad(s):
            if len(s) < N:
                return "".join(["0" for _ in range(N - len(s))]) + s
            else:
                return s

        abin = lpad(abin)
        bbin = lpad(bbin)
        cbin = lpad(cbin)

        def countMinFlips(i):
            if i == N:
                return 0
            abit = int(abin[i])
            bbit = int(bbin[i])
            cbit = int(cbin[i])

            ans = 0
            if abit | bbit == cbit:
                ans = countMinFlips(i + 1)
            elif (abit + 1) % 2 | bbit == cbit or abit | (bbit + 1) % 2 == cbit:
                ans = 1 + countMinFlips(i + 1)
            else:
                ans = 2 + countMinFlips(i + 1)
            return ans

        return countMinFlips(0)


# leetcode submit region end(Prohibit modification and deletion)


class MinimumFlipsToMakeAOrBEqualToC(Solution):
    pass
