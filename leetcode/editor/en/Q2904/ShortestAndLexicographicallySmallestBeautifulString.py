import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        left = 0
        right = 0
        N = len(s)
        found = False
        ans = (1 << (N * 2))
        current_window_number = (1 << (N + 1))
        while right < N:
            current_pos = N - right
            if s[right] == "1":
                current_window_number ^= (1 << current_pos)
            while current_window_number.bit_count() > k + 1:
                to_be_zero = N - left
                if current_window_number & (1 << to_be_zero) != 0:
                    current_window_number ^= (1 << to_be_zero)
                left += 1
            if current_window_number.bit_count() == k + 1:
                if not found:
                    ans = current_window_number
                    found = True
                else:
                    ans_str = bin(ans)[3::].strip("0")
                    current_str = bin(current_window_number)[3::].strip("0")
                    if (len(current_str) < len(ans_str)) or \
                            (len(current_str) == len(ans_str) and current_str < ans_str):
                        ans = current_window_number

            right += 1
        if found:
            return bin(ans)[3::].strip("0")

        return ""


# leetcode submit region end(Prohibit modification and deletion)


class ShortestAndLexicographicallySmallestBeautifulString(Solution):
    pass
