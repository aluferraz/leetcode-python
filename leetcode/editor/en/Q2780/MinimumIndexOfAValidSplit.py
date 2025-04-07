import collections
from typing import List

import sortedcontainers


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        def get_dominant(arr):
            N = len(arr)
            dominant = [-1] * N
            dominant_track = sortedcontainers.SortedList()
            cnt = collections.Counter()
            for i in range(N):
                dominant_track.discard((cnt[arr[i]], arr[i]))
                cnt[arr[i]] += 1
                dominant_track.add((cnt[arr[i]], arr[i]))
                if dominant_track[-1][0] > ((i + 1) // 2):
                    dominant[i] = dominant_track[-1][1]

            return dominant

        dominant_ltr = get_dominant(nums)
        dominant_rtl = get_dominant(list(reversed(nums)))
        dominant_rtl.reverse()
        N = len(nums)

        for i in range(N - 1):
            if dominant_ltr[i] == dominant_rtl[i + 1] and dominant_ltr[i] >= 0:
                return i
        return -1


# leetcode submit region end(Prohibit modification and deletion)


class MinimumIndexOfAValidSplit(Solution):
    pass
