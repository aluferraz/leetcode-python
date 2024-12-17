import heapq
import math
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-x for x in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            max_n = abs(heapq.heappop(gifts))
            heapq.heappush(gifts, -1 * (math.floor(math.sqrt(max_n))))
        return sum(abs(x) for x in gifts)


# leetcode submit region end(Prohibit modification and deletion)


class TakeGiftsFromTheRichestPile(Solution):
    pass
