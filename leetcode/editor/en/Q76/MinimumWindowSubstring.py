import collections
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        cnt_1 = collections.defaultdict(int)
        for c in t:
            cnt_1[c] += 1

        cnt_window = collections.defaultdict(int)
        def compare_cnt():
            for c in cnt_1.keys():
                if cnt_window[c] < cnt_1[c]:
                    return False
            return True

        left = 0
        right = 0
        N = len(s)
        ans = (0, N)
        while right < N:
            cnt_window[s[right]] += 1
            while compare_cnt() and left <= right:
                if ans[1] - ans[0] > right - left:
                    ans = (left, right)
                cnt_window[s[left]] -= 1
                left += 1
            right += 1
        if ans[1] == N:
            return ""
        return s[ans[0]:(ans[1]+1)]


# leetcode submit region end(Prohibit modification and deletion)


class MinimumWindowSubstring(Solution):
    pass