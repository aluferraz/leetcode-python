import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = collections.Counter(arr)
        seen = set()
        for v in cnt.values():
            if v in seen:
                return False
            seen.add(v)
        return True

# leetcode submit region end(Prohibit modification and deletion)


class UniqueNumberOfOccurrences(Solution):
    pass
