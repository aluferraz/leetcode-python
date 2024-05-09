from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        N = len(score)
        ranks = sorted([(-score[i], i) for i in range(N)])
        ranks_name = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        ans = [""] * N
        for i in range(N):
            _, pos = ranks[i]
            if i < len(ranks_name):
                ans[pos] = ranks_name[i]
            else:
                ans[pos] = str(i + 1)

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class RelativeRanks(Solution):
    pass
