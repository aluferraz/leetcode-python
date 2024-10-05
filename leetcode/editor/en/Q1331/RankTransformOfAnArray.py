from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        N = len(arr)
        ranked = sorted([(x, i) for i, x in enumerate(arr)])
        ans = [0] * N
        rank = 0
        prev = -(10 ** 20)
        for _, i in ranked:
            if ans[i] > prev:
                rank += 1
            ans[i] = rank
            prev = ans[i]
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class RankTransformOfAnArray(Solution):
    pass
