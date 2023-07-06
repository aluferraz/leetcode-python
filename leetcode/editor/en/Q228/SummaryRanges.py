from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        ans = []
        N = len(nums)
        if N == 0:
            return ans
        curr = [nums[0], nums[0]]

        def push(el):
            if el[0] != el[1]:
                ans.append(str(el[0]) + "->" + str(el[1]))
            else:
                ans.append(str(el[0]))

        if N == 1:
            push(curr)
        for i in range(1, N):
            if nums[i] != nums[i - 1] + 1:
                push(curr)
                curr = [nums[i], nums[i]]
            else:
                curr[1] = nums[i]
            if i == N - 1:
                push(curr)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class SummaryRanges(Solution):
    pass
