import collections
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """

        substrings = collections.defaultdict(list)
        N = len(s)
        last_pos = 0
        counter = 1
        for i in range(1, N):
            if s[i] != s[i - 1]:
                substrings[s[i - 1]].append(-counter)
                counter = 1
            else:
                counter += 1
        substrings[s[- 1]].append(-counter)
        ans = -1
        for k, v in substrings.items():
            heapq.heapify(v)
            a = abs(heapq.heappop(v))
            if a >= 3:
                ans = max(ans, (a - 3 + 1))
            if len(v) > 0:
                b = abs(heapq.heappop(v))
                # if a % 2 == 0:
                #     ans = max(ans, min((a // 2), b))
                # else:
                ans = max(ans, min((a - 1), b))
                # if b % 2 == 0:
                #     ans = max(ans, min(a, b // 2))
                # else:
                ans = max(ans, min((b - 1), a))
                if len(v) > 0:
                    c = abs(heapq.heappop(v))
                    ans = max(ans, min(a, b, c))

        return ans if ans > 0 else -1

    # leetcode submit region end(Prohibit modification and deletion)


class FindLongestSpecialSubstringThatOccursThriceI(Solution):
    pass
