from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        INF = 10 ** 20

        def find_min(start, end):
            left = start
            right = end
            ans = INF
            if end == start:
                return nums[start]

            while left <= right:
                mid = (left + right) // 2
                ans = min(ans, nums[mid])
                if mid + 1 <= end:
                    if nums[mid + 1] < nums[mid]:
                        return min(
                            find_min(start, mid - 1),
                            find_min(mid + 1, end)
                        )
                    elif nums[mid + 1] > nums[mid]:
                        right = mid - 1
                    else:  # they are equal
                        return min(
                            find_min(start, mid - 1),
                            find_min(mid + 1, end)
                        )
                if mid - 1 >= start:
                    if nums[mid - 1] < nums[mid]:
                        return min(
                            find_min(start, mid - 1),
                            find_min(mid + 1, end)
                        )
                    elif nums[mid - 1] > nums[mid]:
                        left = mid + 1
                    else:  # they are equal
                        return min(
                            find_min(start, mid - 1),
                            find_min(mid + 1, end)
                        )

            return ans

        return find_min(0, N - 1)


# leetcode submit region end(Prohibit modification and deletion)


class FindMinimumInRotatedSortedArrayIi(Solution):
    pass
