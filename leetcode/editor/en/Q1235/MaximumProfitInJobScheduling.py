from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        info_arr = []

        N = len(startTime)

        for i in range(N):
            info_arr.append((startTime[i], endTime[i], profit[i]))

        info_arr.sort(key=lambda x: (x[0], x[1], -x[2]))

        def bin_search(left, target):
            right = N - 1
            ans = N
            while left <= right:
                mid = (left + right) // 2
                if info_arr[mid][0] >= target:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans

        has_cache = [False] * N
        cache = [0] * N

        def go(i):
            if i >= N:
                return 0
            if has_cache[i]:
                return cache[i]

            start, end, earn = info_arr[i]

            take_job = earn + go(bin_search(i + 1, end))
            skip = go(i + 1)

            ans = max(take_job, skip)

            has_cache[i] = True
            cache[i] = ans

            return ans

        return go(0)

        # leetcode submit region end(Prohibit modification and deletion)


class MaximumProfitInJobScheduling(Solution):
    pass
