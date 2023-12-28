from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        N = len(s)
        encoding_cnt = []

        i = 0
        while i < N:
            j = i + 1
            while j < N and s[j] == s[i]:
                j += 1
            cnt = j - i
            encoding_cnt.append((s[i], cnt))
            i = j
        INF = 10 ** 20

        cache = {}

        def go(i, k, prev_cnt, prev_char):
            if i == len(encoding_cnt):
                return 0
            if (i, k, prev_cnt, prev_char) in cache:
                return cache[(i, k, prev_cnt, prev_char)]
            c, cnt_here = encoding_cnt[i]
            ans = INF
            for j in range(min(k + 1, cnt_here + 1)):
                new_cnt = cnt_here - j
                correction = 0

                if prev_char == c:
                    if prev_cnt == 1:
                        correction = 1
                    else:
                        correction = (1 + len(str(prev_cnt)))
                    new_cnt += prev_cnt
                new_len = 1 + len(str(new_cnt))

                if new_cnt == 1:
                    new_len = 1
                new_prev_char = c
                new_prev_cnt = new_cnt
                if new_cnt == 0:
                    new_len = 0
                    new_prev_cnt = prev_cnt
                    new_prev_char = prev_char
                ans_here = (new_len + go(i + 1, k - j, new_prev_cnt, new_prev_char)) - correction

                ans = min(ans, ans_here)
            cache[(i, k, prev_cnt, prev_char)] = ans
            return ans

        return go(0, k, 0, "")


# leetcode submit region end(Prohibit modification and deletion)


class StringCompressionIi(Solution):
    pass
