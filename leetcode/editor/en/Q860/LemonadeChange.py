import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        available_bills = collections.defaultdict(int)
        total_available = 0
        options = [20, 10, 5]
        for b in bills:
            change = b - 5
            while change > 0:
                used = False
                for op in options:
                    if available_bills[op] > 0 and op <= change:
                        used = True
                        needed_bills = (change // op)
                        can_use = min(needed_bills, available_bills[op])
                        change -= (can_use * op)
                        available_bills[op] -= can_use
                        total_available -= (can_use * op)
                        break
                if total_available == 0 or not used:
                    return False
            available_bills[b] += 1
            total_available += b
        return True


# leetcode submit region end(Prohibit modification and deletion)


class LemonadeChange(Solution):
    pass
