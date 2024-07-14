# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        N = len(s)
        cache = [(-1, '')] * N

        def go(i):
            if i >= N:
                return (0, '')
            if cache[i][0] >= 0:
                return cache[i]
            next_tot, next_c = go(i + 1)
            ans_here = next_tot
            if s[i] + next_c == 'ab':
                ret_ahead = go(i + 2)
                total = x + ret_ahead[0]
                if total > ans_here:
                    cache[i] = (total, ret_ahead[1])
                    return cache[i]
            if s[i] + next_c == 'ba':
                ret_ahead = go(i + 2)
                total = y + ret_ahead[0]
                if total > ans_here:
                    cache[i] = (total, ret_ahead[1])
                    return cache[i]

            cache[i] = (ans_here, s[i])
            return cache[i]

        return go(0)


# leetcode submit region end(Prohibit modification and deletion)


class MaximumScoreFromRemovingSubstrings(Solution):
    pass
