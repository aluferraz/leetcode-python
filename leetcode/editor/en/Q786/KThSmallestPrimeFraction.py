import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fract = []
        N = len(arr)
        for i in range(N):
            for j in range(i + 1, N):
                fract.append((arr[i] / arr[j], arr[i], arr[j]))
        heapq.heapify(fract)
        ans = []
        for i in range(k):
            _, a, b = heapq.heappop(fract)
            ans = [a, b]
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class KThSmallestPrimeFraction(Solution):
    pass
