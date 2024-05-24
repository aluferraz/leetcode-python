import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        counter = collections.defaultdict(int)

        def go(i, cnt):
            if i == N:
                return 1 if len(cnt) > 0 else 0
            num = nums[i]
            ans_here = go(i + 1, cnt)
            if (num - k) not in cnt:
                cnt[num] += 1
                ans_here += go(i + 1, cnt)
                cnt[num] -= 1
                if cnt[num] == 0:
                    cnt.pop(num)
            return ans_here

        return go(0, counter)


# leetcode submit region end(Prohibit modification and deletion)


class TheNumberOfBeautifulSubsets(Solution):
    pass
