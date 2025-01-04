import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = set()
        N = len(nums)
        nums_heap = [(nums[i], i) for i in range(N)]
        heapq.heapify(nums_heap)
        score = 0
        while nums_heap:
            s, i = heapq.heappop(nums_heap)
            while nums_heap and i in marked:
                s, i = heapq.heappop(nums_heap)
            if i not in marked:
                marked.add(i)
                marked.add(i - 1)
                marked.add(i + 1)
                score += s
        return score


# leetcode submit region end(Prohibit modification and deletion)


class FindScoreOfAnArrayAfterMarkingAllElements(Solution):
    pass
