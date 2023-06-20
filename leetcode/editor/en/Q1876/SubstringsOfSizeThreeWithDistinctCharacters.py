import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        window = collections.deque()
        windowMap = collections.defaultdict(int)
        ans = 0
        for i in range(len(s)):
            window.append(s[i])
            windowMap[s[i]] += 1
            if len(window) < 3:
                continue
            if len(window) > 3:
                outside = window.popleft()
                windowMap[outside] -= 1
                if windowMap[outside] == 0:
                    windowMap.pop(outside)
            if len(windowMap) == 3:
                ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class SubstringsOfSizeThreeWithDistinctCharacters(Solution):
    pass
