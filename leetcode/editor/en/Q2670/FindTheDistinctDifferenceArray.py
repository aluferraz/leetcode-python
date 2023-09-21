from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:

        prefix_dist = []
        suffix_dist = []
        N = len(nums)
        pset = set()
        sset = set()
        for i in range(N):
            pset.add(nums[i])
            prefix_dist.append(len(pset))
            sset.add(nums[N - i - 1])
            suffix_dist.append(len(sset))
        suffix_dist.reverse()
        ans = []
        for i in range(N - 1):
            ans.append(prefix_dist[i] - suffix_dist[i + 1])
        ans.append(prefix_dist[-1])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class FindTheDistinctDifferenceArray(Solution):
    pass
