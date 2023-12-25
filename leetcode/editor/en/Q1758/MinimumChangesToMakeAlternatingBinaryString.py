from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        s = [int(c) for c in s]

        def go(prev, i):
            if i == N:
                return 0
            target = (prev + 1) % 2
            if s[i] == target:
                return go(s[i], i + 1)
            return 1 + go(target, i + 1)

        return min(go(0, 0), go(1, 0))

        # leetcode submit region end(Prohibit modification and deletion)


class MinimumChangesToMakeAlternatingBinaryString(Solution):
    pass
