from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        N = len(words)
        for i in range(N):
            for j in range(i + 1, N):
                if words[i] in words[j]:
                    ans.append(words[i])
                    break
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class StringMatchingInAnArray(Solution):
    pass
