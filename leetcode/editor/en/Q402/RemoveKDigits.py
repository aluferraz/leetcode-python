from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ans = []
        N = len(num)
        if k >= N:
            return "0"
        final_len = N - k
        for i in range(N):
            digit = int(num[i])
            while len(ans) > 0 and digit < ans[-1] and ((N - (i + 1)) + len(ans)) >= final_len:
                ans.pop()
            ans.append(digit)
        while len(ans) > final_len:
            ans.pop()

        ans_s = "".join(str(d) for d in ans)
        left = 0
        while left < (len(ans_s) - 1) and ans_s[left] == "0":
            left += 1
        return ans_s[left::]



# leetcode submit region end(Prohibit modification and deletion)


class RemoveKDigits(Solution):
    pass