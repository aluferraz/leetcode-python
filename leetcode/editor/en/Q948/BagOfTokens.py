from functools import cache
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        N = len(tokens)
        INF = 10 ** 20
        tokens.sort()
        left = 0
        right = N-1

        score = 0
        while left <= right:
            if tokens[left] <= power:
                score += 1
                power -= tokens[left]
                left += 1
            elif score >= 1 and right - left > 1:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
        return score


# leetcode submit region end(Prohibit modification and deletion)


class BagOfTokens(Solution):
    pass