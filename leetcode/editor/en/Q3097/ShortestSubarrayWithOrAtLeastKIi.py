from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        curr = {}  # Mapping from OR value to minimal length
        res = N + 1  # Initialize result to a large value

        for num in nums:
            temp = {}
            # Update OR values for subarrays ending at the current position
            for or_value, length in curr.items():
                new_or = or_value | num
                new_len = length + 1
                if new_or not in temp or temp[new_or] > new_len:
                    temp[new_or] = new_len
            # Start a new subarray at the current position
            if num not in temp or temp[num] > 1:
                temp[num] = 1
            # Check if any OR value meets or exceeds k
            for or_value, length in temp.items():
                if or_value >= k:
                    res = min(res, length)
            curr = temp

        return res if res <= N else -1


# leetcode submit region end(Prohibit modification and deletion)


class ShortestSubarrayWithOrAtLeastKIi(Solution):
    pass
