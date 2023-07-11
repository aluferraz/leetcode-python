import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestVariance(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        ans = 0
        for i in range(26):
            for j in range(26):
                if j == i:
                    continue
                windowSum = 0
                window = collections.deque()
                dominatingCount = 0
                for k in range(N):
                    ch = s[k]
                    diff = 0
                    if ch == chr(i + ord('a')):
                        diff -= 1
                    elif ch == chr(j + ord('a')):
                        diff += 1
                    while dominatingCount > 0 and windowSum + diff < diff and diff > 0:
                        toRemove, idx = window[0]
                        if dominatingCount + min(toRemove, 0) == 0:
                            break
                        windowSum -= toRemove
                        dominatingCount += min(toRemove, 0)
                        window.popleft()
                    window.append((diff, k))
                    windowSum += diff
                    if dominatingCount > 0:
                        ans = max(ans, windowSum)
                    if diff == -1:
                        dominatingCount += 1
                if dominatingCount > 0:
                    ans = max(ans, windowSum)
        return max(ans, 0)


# leetcode submit region end(Prohibit modification and deletion)


class SubstringWithLargestVariance(Solution):
    pass
