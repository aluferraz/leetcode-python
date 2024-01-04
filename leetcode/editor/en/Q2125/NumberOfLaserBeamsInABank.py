from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        N = len(bank)

        bank_int = []
        for i in range(N):
            row = sum([int(x) for x in bank[i]])
            if row == 0:
                continue
            bank_int.append(row)
        ans = 0
        M = len(bank_int)
        for i in range(1, M):
            ans_here = (bank_int[i-1] * bank_int[i])
            ans += ans_here
        return ans



# leetcode submit region end(Prohibit modification and deletion)


class NumberOfLaserBeamsInABank(Solution):
    pass
