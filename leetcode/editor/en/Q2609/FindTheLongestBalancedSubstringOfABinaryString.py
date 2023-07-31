import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        window = collections.deque()
        best = 0
        N = len(s)
        last_one = -1
        total = 0
        for i in range(N):
            if s[i] == '0':
                if last_one < i:
                    while len(window) > 0 and window[0] <= last_one:
                        total -= int(s[window.popleft()])
                    last_one = -1
                window.append(i)
            elif s[i] == '1' and len(window) > 0:
                last_one = max(last_one, i)
                total += 1
                window.append(i)
            total_zeros = len(window) - total
            total_ones = total
            if total_zeros > 0 and total_ones > 0:
                can_use = min(total_ones, total_zeros)
                best = max(best, can_use * 2)
        return best


# leetcode submit region end(Prohibit modification and deletion)


class FindTheLongestBalancedSubstringOfABinaryString(Solution):
    pass
