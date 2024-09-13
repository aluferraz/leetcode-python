from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0

        def to_arr(s):
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] = 1
            return arr

        allowed = to_arr(allowed)
        for w in words:
            w_arr = to_arr(w)
            valid = True
            for i in range(26):
                if w_arr[i] == 1 and allowed[i] == 0:
                    valid = False
                    break
            if valid:
                ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class CountTheNumberOfConsistentStrings(Solution):
    pass
