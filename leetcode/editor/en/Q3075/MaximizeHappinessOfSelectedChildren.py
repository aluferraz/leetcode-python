import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happyheap = [-h for h in happiness]
        heapq.heapify(happyheap)
        ans = 0
        for i in range(min(k, len(happiness))):
            ans += max(0, abs(heapq.heappop(happyheap)) - i)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MaximizeHappinessOfSelectedChildren(Solution):
    pass
