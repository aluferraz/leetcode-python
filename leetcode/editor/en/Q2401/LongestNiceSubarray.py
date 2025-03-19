from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        N = len(nums)

        def good(size):
            counter = [0] * 32
            left = 0
            right = 0

            while right < N:
                for i in range(32):
                    if (1 << i) & nums[right] != 0:
                        counter[i] += 1
                if (right - left) + 1 > size:
                    for i in range(32):
                        if (1 << i) & nums[left] != 0:
                            counter[i] -= 1
                    left += 1
                if (right - left) + 1 == size:
                    valid = True
                    for i in range(32):
                        if counter[i] > 1:
                            valid = False
                            break
                    if valid:
                        return True
                right += 1
            return False

        left = 0
        right = N + 1
        ans = 0
        while left < right:
            mid = (left + right) // 2
            if good(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class LongestNiceSubarray(Solution):
    pass
