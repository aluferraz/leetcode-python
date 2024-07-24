import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = sorted(collections.Counter(nums).items(), key=lambda x: (x[1], -x[0]))
        ans = []
        for n, tot in cnt:
            for _ in range(tot):
                ans.append(n)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class SortArrayByIncreasingFrequency(Solution):
    pass
