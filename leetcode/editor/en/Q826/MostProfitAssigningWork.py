from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        combo = list(zip(difficulty, profit))
        combo.sort()
        N = len(combo)
        max_d = combo[-1][0]
        max_prof = [0] * (max_d + 1)
        j = 0
        for i in range(1, (max_d + 1)):
            max_p = max_prof[i - 1]
            while j < N and combo[j][0] == i:
                max_p = max(combo[j][1], max_p)
                j += 1
            max_prof[i] = max_p
        ans = 0
        for w in worker:
            ans += max_prof[min(w, max_d)]
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MostProfitAssigningWork(Solution):
    pass
