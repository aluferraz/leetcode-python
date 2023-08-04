from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        dmap = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z'],
            "0": [' '],
        }

        ans = []
        N = len(digits)
        current = []

        def go(i):
            if i == N:
                if len(current) > 0:
                    ans.append("".join(current))
                return

            for c in dmap[digits[i]]:
                current.append(c)
                go(i + 1)
                current.pop()

        go(0)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class LetterCombinationsOfAPhoneNumber(Solution):
    pass
