from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:

        def get_cnt(s):
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord('a')] += 1
            return cnt
        target_cnt = get_cnt(target)
        N = len(stickers)
        stickers_cnt = [[] for _ in range(N)]
        for i in range(N):
            stickers_cnt[i] = get_cnt(stickers[i])

        def count_match(cur_target, sticker_cnt):
            matches = 0
            for i in range(26):
                if cur_target[i] > 0:
                    matches += min(cur_target[i], sticker_cnt[i])
            return matches

        def subtract(a,b):
            ans = list(a)
            for i in range(26):
                ans[i] -= b[i]
                ans[i] = max(ans[i], 0)
            return ans

        INF = 10 ** 20
        cache = {}
        def solve(target_cnt_cur):
            if sum(target_cnt_cur) == 0:
                return 0
            cache_key = "".join([str(c) for c in target_cnt_cur])
            if cache_key in cache:
                return cache[cache_key]
            ans = INF
            for i in range(N):
                sticker_cnt = stickers_cnt[i]
                match_here = count_match(target_cnt_cur,sticker_cnt)
                if match_here > 0:
                    ans = min(ans, 1 + solve(subtract(target_cnt_cur, sticker_cnt)))
            cache[cache_key] = ans
            return ans
        ans = solve(target_cnt)
        if ans >= INF:
            return -1
        return ans

# leetcode submit region end(Prohibit modification and deletion)


class StickersToSpellWord(Solution):
    pass