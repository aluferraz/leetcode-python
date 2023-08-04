from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # a + b > c
        # b + c > a
        # a + c > b

        nums.sort()

        N = len(nums)
        ans = 0

        def find_idx(left, max):
            right = N - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= max:
                    right = mid - 1
                else:
                    ans = mid
                    left = mid + 1
            return ans

        for i in range(N):
            for j in range(i - 1, -1, -1):
                pair = nums[i] + nums[j]
                idx = find_idx(i + 1, pair)
                if idx != -1:
                    ans += (idx - i)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class ValidTriangleNumber(Solution):
    pass
