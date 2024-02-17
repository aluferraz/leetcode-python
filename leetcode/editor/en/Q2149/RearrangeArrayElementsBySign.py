import collections
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = collections.deque()
        neg = collections.deque()
        N = len(nums)
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        ans = []
        while len(ans) < N:
            if (len(ans) == 0 or ans[-1] < 0) and len(pos) > 0:
                ans.append(pos.popleft())
            else:
                ans.append(neg.popleft())
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class RearrangeArrayElementsBySign(Solution):
    pass