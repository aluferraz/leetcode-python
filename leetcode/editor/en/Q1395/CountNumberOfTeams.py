from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)

        cache = {}

        def go(i, p, dec):
            if i >= N:
                return 0
            ans_here = go(i + 1, p, dec)
            if dec:
                if rating[i] < rating[p]:
                    ans_here += 1 + go(i + 1, i, dec)
            else:
                if rating[i] > rating[p]:
                    ans_here += 1 + go(i + 1, i, dec)
            return ans_here

        ans = 0
        for i in range(N):
            inc = go(i, i, False)
            dec = go(i, i, True)
            ans += inc + dec
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class CountNumberOfTeams(Solution):
    pass
