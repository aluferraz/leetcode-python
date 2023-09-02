import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        N = len(s)
        q = collections.deque([i for i in range(N + 1)])
        ans = []
        for c in s:
            if c == 'I':
                ans.append(q.popleft())
            else:
                ans.append(q.pop())
        ans.append(q.pop())
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class DiStringMatch(Solution):
    pass
