# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = []
        i = 0
        N = len(word)
        while i < N:
            ans.append(word[i])
            if word[i] == ch:
                ans.reverse()
                break
            i += 1
        i += 1
        while i < N:
            ans.append(word[i])
            i += 1
        return "".join(ans)


# leetcode submit region end(Prohibit modification and deletion)


class ReversePrefixOfWord(Solution):
    pass
