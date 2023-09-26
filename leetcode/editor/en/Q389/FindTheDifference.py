from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        N = len(t)
        for i in range(N):
            cnt1[ord(t[i]) - ord('a')] += 1
            if i < N - 1:
                cnt2[ord(s[i]) - ord('a')] += 1
        for i in range(26):
            if cnt1[i] != cnt2[i]:
                return chr(i + ord('a'))
        return ''


# leetcode submit region end(Prohibit modification and deletion)


class FindTheDifference(Solution):
    pass
