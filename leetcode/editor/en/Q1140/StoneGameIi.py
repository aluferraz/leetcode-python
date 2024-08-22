from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)

        cache = {}

        def go(i, M, player):
            if i == N:
                return (0, 0)
            if (i, M, player) in cache:
                return cache[(i, M, player)]
            best = (0, 0)
            sum_here = 0
            for j in range(i, min(i + M, N)):
                new_m = j - i + 1
                sum_here += piles[j]
                new_m_bounded = min(max(2 * new_m, M), N - j)
                alice, bob = go(j + 1, new_m_bounded, (player + 1) % 2)
                take = [alice, bob]
                take[player] += sum_here
                if take[player] >= best[player]:
                    best = (take[0], take[1])
            cache[(i, M, player)] = best
            return best

        ans = go(0, 2, 0)[0]
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class StoneGameIi(Solution):
    pass
