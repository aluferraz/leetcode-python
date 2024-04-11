import collections
import heapq
from typing import List

import sortedcontainers


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        ans = [None] * N
        heapq.heapify(deck)
        stack = collections.deque( [i for i in range(N)])
        def shuffle_cards(should_stack):
            if len(deck) == 0:
                return
            next_idx = stack.popleft()
            if should_stack:
                stack.append(next_idx)
            else:
                ans[next_idx] = heapq.heappop(deck)
            return shuffle_cards(not should_stack)
        shuffle_cards(False)
        return ans







# leetcode submit region end(Prohibit modification and deletion)


class RevealCardsInIncreasingOrder(Solution):
    pass
