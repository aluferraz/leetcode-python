from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        N = len(nums)

        def bin_search_inc(left, right):
            start = left
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= nums[start]:
                    left = mid + 1
                else:
                    right = mid
            return left

        def bin_search_exc(left, right, good):
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if good(mid):
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        found = False

        def divide_and_conquer(left, right):
            if left == right:
                return N - 1
            if nums[left] == nums[right]:
                mid = (left + right) // 2
                left_part = divide_and_conquer(left, mid)
                right_part = divide_and_conquer(mid + 1, right)

                ans = min(
                    left_part,
                    right_part
                )
                return ans
            else:
                nonlocal found
                if nums[left] < nums[right]:
                    found = found or bin_search_exc(left, right, lambda x: nums[x] == target) >= 0
                    return left
                pivot = bin_search_inc(left, right)
                found = found or max(bin_search_exc(left, pivot, lambda x: nums[x] == target),
                                     bin_search_exc(pivot, right, lambda x: nums[x] == target)) >= 0
                return pivot

        divide_and_conquer(0, N - 1)

        return found or bin_search_exc(0, N - 1, lambda x: nums[x] == target) >= 0

    # leetcode submit region end(Prohibit modification and deletion)


class SearchInRotatedSortedArrayIi(Solution):
    pass
