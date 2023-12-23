import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """

        ans = 0
        chars = collections.defaultdict(int)
        window = collections.deque()

        for c in s:
            chars[c] += 1
            window.append(c)
            while len(chars) > 2:
                left = window.popleft()
                chars[left] -= 1
                if chars[left] == 0:
                    chars.pop(left)
            ans = max(ans, len(window))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class LongestSubstringWithAtMostTwoDistinctCharacters(Solution):
    pass
