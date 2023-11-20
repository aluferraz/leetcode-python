import collections
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        counter = collections.defaultdict(int)
        N = len(nums)
        for i in range(N):
            counter[nums[i]] += 1
        distinct = list(counter.keys())
        distinct.sort()
        ans = 0
        while len(distinct) > 1:
            num = distinct.pop()
            ans += counter[num]
            next_num = distinct[-1]
            counter[next_num] += counter[num]
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class ReductionOperationsToMakeTheArrayElementsEqual(Solution):
    pass
