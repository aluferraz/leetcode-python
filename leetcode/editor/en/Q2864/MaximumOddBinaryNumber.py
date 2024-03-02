from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zeros = s.count("0")
        ones = s.count("1")
        ans = []
        for _ in range(ones - 1):
            ans.append("1")
        for _ in range(zeros):
            ans.append("0")
        ans.append("1")
        return "".join(ans)
# leetcode submit region end(Prohibit modification and deletion)


class MaximumOddBinaryNumber(Solution):
    pass