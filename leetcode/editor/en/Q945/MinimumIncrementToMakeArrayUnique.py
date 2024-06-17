import collections
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        N = len(nums)
        cnt = collections.Counter(nums)
        empty_slots = []
        max_number = nums[-1]
        max_seen = nums[-1]
        for i in range(max_number, -1, -1):
            num = i
            if cnt[num] > 1:
                while cnt[num] > 1:
                    next_slot = 0
                    if len(empty_slots) > 0:
                        next_slot = heapq.heappop(empty_slots)
                    else:
                        max_seen += 1
                        next_slot = max_seen
                    ans += next_slot - num
                    cnt[num] -= 1
                    cnt[next_slot] += 1
            elif cnt[num] == 0:
                heapq.heappush(empty_slots, num)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MinimumIncrementToMakeArrayUnique(Solution):
    pass
