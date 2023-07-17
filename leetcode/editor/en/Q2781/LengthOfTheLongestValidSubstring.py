import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestValidSubstring(self, word, forbidden):
        """
        :type word: str
        :type forbidden: List[str]
        :rtype: int
        """
        forbidden = set(forbidden)
        N = len(word)
        window = collections.deque()
        left = 0
        right = 0
        ans = 0
        while right <= N:
            for i in range(1, 11):
                check = "".join(word[max(right - i, left):right])
                while check in forbidden:
                    left += 1
                    check = "".join(word[max(right - i, left):right])
            ans = max(ans, (right - left))
            right += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class LengthOfTheLongestValidSubstring(Solution):
    pass
