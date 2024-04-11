from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ans = []
        N = len(num)
        final_len = N - k
        for i in range(N):
            digit = int(num[i])
            while len(ans) > 0 and digit < ans[-1] and (N - i + len(ans) ) >= final_len:
                ans.pop()
            ans.append(digit)
        return "".join(ans)


# leetcode submit region end(Prohibit modification and deletion)


class RemoveKDigits(Solution):
    pass