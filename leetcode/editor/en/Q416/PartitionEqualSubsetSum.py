import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        q = collections.deque([(0, 0, 0)])
        seen = {(0, 0, 0)}
        while q:
            size = len(q)
            for i in range(size):
                idx, l, r = q.pop()
                if idx == N:
                    if l == r:
                        return True
                    continue
                use = (idx + 1, l + nums[idx], r)
                if use not in seen:
                    seen.add(use)
                    q.append(use)
                skip = (idx + 1, l, r + nums[idx])
                if skip not in seen:
                    seen.add(skip)
                    q.append(skip)
        return False


# leetcode submit region end(Prohibit modification and deletion)


class PartitionEqualSubsetSum(Solution):
    pass
