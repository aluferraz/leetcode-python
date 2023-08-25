from functools import cache
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """

        @cache
        def go(i, j):
            if i == len(abbr) and j == len(word):
                return True
            if i >= len(abbr) or j >= len(word):
                return False

            if abbr[i].isalpha():
                return word[j] == abbr[i] and go(i + 1, j + 1)
            else:
                if abbr[i] == '0':
                    return False
                number_arr = []
                while i < len(abbr) and abbr[i].isdigit():
                    number_arr.append(abbr[i])
                    i += 1
                number = int("".join(number_arr))
                if go(i, j + number):
                    return True
                return False

        return go(0, 0)


# leetcode submit region end(Prohibit modification and deletion)


class ValidWordAbbreviation(Solution):
    pass
