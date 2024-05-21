from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        N = len(nums)

        def go(i, cur):
            if i >= N:
                ans.append(list(cur))
                return
            cur.append(nums[i])
            for j in range(i + 1, N + 1):
                go(j, cur)
            cur.pop()

        for i in range(N):
            go(i, [])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class Subsets(Solution):
    pass
