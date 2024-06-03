from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s)
        left = 0
        right = N - 1

        def swap(i, j):
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp

        while left <= right:
            swap(left, right)
            left += 1
            right -= 1


# leetcode submit region end(Prohibit modification and deletion)


class ReverseString(Solution):
    pass
