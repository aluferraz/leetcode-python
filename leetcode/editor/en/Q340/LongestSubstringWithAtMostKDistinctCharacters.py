import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0:
            return ""
        left = 0
        right = 0
        N = len(s)

        counter = collections.defaultdict(int)
        best = (0, 0)
        while right < N:
            i = ord(s[right]) - ord('a')
            counter[i] += 1
            while len(counter) > k:
                leftIdx = ord(s[left]) - ord('a')
                counter[leftIdx] -= 1
                if counter[leftIdx] == 0:
                    counter.pop(leftIdx)
                left += 1
            if (right - left + 1) > (best[1] - best[0] + 1):
                best = (left, right)
            right += 1
        return (best[1] - best[0] + 1)


# leetcode submit region end(Prohibit modification and deletion)


class LongestSubstringWithAtMostKDistinctCharacters(Solution):
    pass
