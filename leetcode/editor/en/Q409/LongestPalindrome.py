import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = collections.Counter(s)
        has_one = 0
        longest = 0
        for c in set(s):
            if cnt[c] % 2 == 0:
                longest += cnt[c]
            else:
                longest += (cnt[c] - 1)
                has_one = 1
        longest += has_one
        return longest


# leetcode submit region end(Prohibit modification and deletion)


class LongestPalindrome(Solution):
    pass
