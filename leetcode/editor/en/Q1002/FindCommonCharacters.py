from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        N = len(words)
        cnt = [[0 for _ in range(26)] for _ in range(N)]
        ans = []
        for i in range(N):
            w = words[i]
            for c in w:
                cnt[i][ord(c) - ord('a')] += 1
        for i in range(26):
            common = cnt[0][i]
            for j in range(N):
                common = min(common, cnt[j][i])
            for _ in range(common):
                ans.append(chr(i + ord('a')))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class FindCommonCharacters(Solution):
    pass
