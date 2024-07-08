import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        N = len(nums)
        queue = collections.deque()
        target = 0
        ans = 0
        for i in range(N):
            if len(queue) > 0 and queue[0] == i:
                queue.popleft()
                target = (target + 1) % 2

            if nums[i] == target:
                # If we see a 0, we want to flip next k 0's to 1's and 1's to 0's
                # So the target becomes a 1 until i+k
                target = (target + 1) % 2
                queue.append(i + k)
                ans += 1
        if len(queue) > 0 and queue[0] == N:
            queue.popleft()
        if len(queue) == 0:
            return ans
        return -1


# leetcode submit region end(Prohibit modification and deletion)


class MinimumNumberOfKConsecutiveBitFlips(Solution):
    pass
