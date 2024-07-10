from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cur_time = customers[0][0]
        wait = 0
        for s, d in customers:
            cur_time = max(s, cur_time)
            cur_time += d
            wait += (cur_time - s)
        N = len(customers)
        return wait / N


# leetcode submit region end(Prohibit modification and deletion)


class AverageWaitingTime(Solution):
    pass
