import math
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minOperations(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if sum(nums) < target:
            return -1
        nums.sort()
        target_bin = bin(target)[2::]
        target_counter = [0] * 32
        nums_counter = [0] * 32
        rev_target_bin = list(target_bin)
        rev_target_bin.reverse()
        for i in range(len(target_bin)):
            target_counter[i] += int(rev_target_bin[i])
        for n in nums:
            nstr = (bin(n)[2::])
            nums_counter[len(nstr) - 1] += 1
        op = 0
        for i in range(len(target_bin)):
            if target_counter[i] == 0:
                continue
            if nums_counter[i] >= target_counter[i]:
                nums_counter[i] -= target_counter[i]
            else:
                for j in range(i):
                    if nums_counter[j] > 1:
                        nums_counter[j + 1] += (nums_counter[j] // 2)
                        nums_counter[j] = 0
                if nums_counter[i] >= target_counter[i]:
                    nums_counter[i] -= target_counter[i]
                else:
                    pos = 0
                    for j in range(i + 1, len(target_counter)):
                        if nums_counter[j] >= 1:
                            pos = j
                            break
                    while nums_counter[i] < target_counter[i]:
                        nums_counter[pos] -= 1
                        nums_counter[pos - 1] += 2
                        pos -= 1
                        op += 1
                    nums_counter[i] -= target_counter[i]

        return op


# leetcode submit region end(Prohibit modification and deletion)


class MinimumOperationsToFormSubsequenceWithTargetSum(Solution):
    pass
