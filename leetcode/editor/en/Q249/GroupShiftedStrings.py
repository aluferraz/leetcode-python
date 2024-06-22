import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        alpha = [''] * 26
        for i in range(26):
            alpha[i] = chr(ord('a') + i)

        def getDistance(c1, c2):
            min_dist = 27
            start = ord(c1) - ord('a')
            dist = 0
            while alpha[start] != c2:
                start += 1
                start %= 26
                dist += 1
            min_dist = dist
            start = ord(c1) - ord('a')
            dist = 0
            while alpha[start] != c2:
                start -= 1
                if start < 0:
                    start = 25
                dist += 1
            if dist < min_dist:
                return -dist
            return min_dist

        keys = collections.defaultdict(list)
        for s in strings:
            diffs = ['0'] * len(s)
            for i in range(1, len(s)):
                diffs[i - 1] = str(getDistance(s[i - 1], s[i]))
            keys[";".join(diffs)].append(s)

        ans = []
        for _, combo in keys.items():
            ans.append(combo)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class GroupShiftedStrings(Solution):
    pass
