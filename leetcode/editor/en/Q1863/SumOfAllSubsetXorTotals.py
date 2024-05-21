from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        N = len(nums)
        subsets = []
        ans = 0

        def go(i, cur):
            if i == N:
                nonlocal ans
                ans += cur
                # subsets.append(list(cur))
            for j in range(i, N):
                # cur.append(nums[i])
                go(j + 1, cur ^ nums[i])
                # cur.pop()

        for i in range(N):
            go(i, 0)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class SumOfAllSubsetXorTotals(Solution):
    pass
