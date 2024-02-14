from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindrome(s):
            left = 0
            right = len(s) - 1
            while left <= right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        for w in words:
            if is_palindrome(w):
                return w
        return ""
# leetcode submit region end(Prohibit modification and deletion)


class FindFirstPalindromicStringInTheArray(Solution):
    pass