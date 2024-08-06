import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = collections.Counter(arr)
        for s in arr:
            if cnt[s] == 1:
                k -= 1
            if k == 0:
                return s
        return ""


# leetcode submit region end(Prohibit modification and deletion)


class KthDistinctStringInAnArray(Solution):
    pass
