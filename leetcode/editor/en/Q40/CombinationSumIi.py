from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        N = len(candidates)
        candidates.sort()
        next_idx = [N] * N
        for i in range(N):
            for j in range(i + 1, N):
                if candidates[j] != candidates[i]:
                    next_idx[i] = j
                    break

        def go(i, target_here, used):
            if target_here == 0:
                return ans.append(list(used))
            if target_here < 0:
                return []
            if i == N:
                return []
            used.append(candidates[i])
            go(i + 1, target_here - candidates[i], used)
            used.pop()
            go(next_idx[i], target_here, used)

        go(0, target, [])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class CombinationSumIi(Solution):
    pass
