import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        N = len(tickets)
        ans = 0
        batches = 0
        before_k = tickets[0:k+1]
        after_k = tickets[k+1:]
        heapq.heapify(before_k)
        heapq.heapify(after_k)
        INF = 10 ** 20
        remaining = tickets[k]
        while batches < remaining:
            min_before = INF if len(before_k) == 0 else before_k[0]
            min_after = INF if len(after_k) == 0 else after_k[0]
            will_remove = min(min_after,min_before)
            reduced = will_remove - batches
            if will_remove == remaining:
                ans += (len(before_k) + len(after_k)) * (reduced - 1)
                ans += (k+1)
                return ans
            else:
                ans += (len(before_k) + len(after_k)) * reduced
            batches += reduced
            while len(before_k) > 0 and batches >= before_k[0]:
                k -= 1
                heapq.heappop(before_k)
            while len(after_k) > 0 and batches >= after_k[0]:
                heapq.heappop(after_k)

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class TimeNeededToBuyTickets(Solution):
    pass
