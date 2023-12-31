from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        last_seen = [N] * 26
        ans = -1

        for i in range(N):
            ch = s[i]
            c = ord(ch) - ord('a')
            ans_here = (i - last_seen[c] - 1)
            ans = max(ans_here, ans)
            last_seen[c] = min(i, last_seen[c])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class LargestSubstringBetweenTwoEqualCharacters(Solution):
    pass
