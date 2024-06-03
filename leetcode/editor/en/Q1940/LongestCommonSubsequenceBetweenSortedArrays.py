from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        ans = []

        def find(arr, target):
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        for i in range(101):
            hits = 0
            for a in arrays:
                if find(a, i) >= 0:
                    hits += 1
            if hits == len(arrays):
                ans.append(i)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class LongestCommonSubsequenceBetweenSortedArrays(Solution):
    pass
