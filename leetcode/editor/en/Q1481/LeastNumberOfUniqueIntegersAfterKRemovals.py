import collections
import heapq
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = collections.Counter(arr)
        heap = []
        for v,c in cnt.most_common():
            heapq.heappush(heap,(c,v))

        for _ in range(k):
            c,v = heapq.heappop(heap)
            c -= 1
            if c == 0:
                continue
            heapq.heappush(heap, (c, v))
        return len(heap)





# leetcode submit region end(Prohibit modification and deletion)


class LeastNumberOfUniqueIntegersAfterKRemovals(Solution):
    pass