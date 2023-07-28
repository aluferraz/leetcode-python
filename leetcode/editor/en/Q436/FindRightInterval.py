from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        N = len(intervals)
        intervals_full = [(r, i) for i, r in enumerate(intervals)]
        intervals_full.sort()

        def find_right(threshold):
            left = 0
            right = N - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if intervals_full[mid][0][0] >= threshold:
                    ans = intervals_full[mid][1]
                    right = mid - 1
                else:
                    left = mid + 1
            return ans

        ans = [-1] * N

        for i in range(N):
            interval, idx = intervals_full[i]
            ans[idx] = find_right(interval[1])
        return ans

    # leetcode submit region end(Prohibit modification and deletion)


class FindRightInterval(Solution):
    pass
