from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)
        ans = []

        def swap(i, j, arr):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

        def go(i):
            if i == N:
                ans.append(list(nums))
                return
            for j in range(i, N):
                swap(i, j, nums)
                go(i + 1)
                swap(i, j, nums)

        go(0)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class Permutations(Solution):
    pass
