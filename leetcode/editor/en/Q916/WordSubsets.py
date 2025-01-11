from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        b = [0] * 26
        for w in words2:
            counter = [0] * 26
            for c in w:
                idx = ord(c) - ord('a')
                counter[idx] += 1
            for i in range(26):
                if counter[i] == 0:
                    continue
                b[i] = max(b[i], counter[i])
        ans = []
        for w in words1:
            counter = [0] * 26
            for c in w:
                idx = ord(c) - ord('a')
                counter[idx] += 1
            good = True
            for i in range(26):
                if b[i] > counter[i]:
                    good = False
                    break
            if good:
                ans.append(w)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class WordSubsets(Solution):
    pass
