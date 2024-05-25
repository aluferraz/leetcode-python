from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        N = len(words)
        counter_words = [[0 for _ in range(26)] for _ in range(N)]
        for i in range(N):
            for c in words[i]:
                counter_words[i][ord(c) - ord('a')] += 1

        score_words = [0] * N
        for i in range(N):
            score_here = 0
            for j in range(26):
                score_here += score[j] * counter_words[i][j]
            score_words[i] = score_here

        def get_allowed_words(counter_letters):
            allowed = 0
            for i in range(N):
                is_allowed = True
                for j in range(26):
                    if counter_letters[j] < counter_words[i][j]:
                        is_allowed = False
                        break
                if is_allowed:
                    allowed |= (1 << i)
            return allowed

        def subtract(a, b):
            ans = list(b)
            for i in range(26):
                ans[i] -= a[i]
            return ans

        cache = {}

        def solve(letters_available, words_used):
            best = 0
            if words_used in cache:
                return cache[words_used]
            words_allowed = get_allowed_words(letters_available)
            if words_allowed == 0:
                return best
            if words_used == (1 << N) - 1:
                return best
            for i in range(N):
                if words_allowed & (1 << i) != 0 and words_used & (1 << i) == 0:
                    remaining = subtract(counter_words[i], letters_available)
                    best = max(best, score_words[i] + solve(remaining, (1 << i) | words_used))
            cache[words_used] = best
            return best

        counter_letters_available = [0] * 26
        for c in letters:
            counter_letters_available[ord(c) - ord('a')] += 1

        return solve(counter_letters_available, 0)


# leetcode submit region end(Prohibit modification and deletion)


class MaximumScoreWordsFormedByLetters(Solution):
    pass
