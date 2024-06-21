from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        N = len(customers)
        guaranteed = 0
        for i in range(N):
            if grumpy[i] == 0:
                guaranteed += customers[i]
                customers[i] = 0

        best = 0
        left = 0
        right = 0
        current_sum = 0
        while right < N:
            current_sum += customers[right]
            while (right - left + 1) > minutes:
                current_sum -= customers[left]
                left += 1
            best = max(best, current_sum)
            right += 1
        return guaranteed + best


# leetcode submit region end(Prohibit modification and deletion)


class GrumpyBookstoreOwner(Solution):
    pass
