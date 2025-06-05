# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def answerString(self, word: str, num_friends: int) -> str:
        n = len(word)
        if num_friends > n:
            return ""
        if num_friends == 1:
            return word

        highest_char = max(word)  # the best single letter we can start with
        best = ""

        for i, ch in enumerate(word):
            if ch != highest_char:
                continue

            remaining = num_friends - (i + 1)  # friends still waiting to cut

            if remaining <= 0:
                # everyone has already “cut” in or before this position,
                # so we can keep the whole suffix
                candidate = word[i:]
            else:
                # leave at least `remaining` letters after our slice
                # end index is exclusive, so this is safe
                candidate = word[i:n - remaining]

            best = max(best, candidate)

        return best


# leetcode submit region end(Prohibit modification and deletion)


class FindTheLexicographicallyLargestStringFromTheBoxI(Solution):
    pass
