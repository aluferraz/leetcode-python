from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        M = len(nums[0])
        nums = set(nums)

        def go(i, arr):
            if i == M:
                number = "".join([str(x) for x in arr])
                if number in nums:
                    return False, ""
                else:
                    return True, number
            arr.append("0")
            found, number = go(i + 1, arr)
            if found:
                return found, number
            arr.pop()
            arr.append("1")
            found, number = go(i + 1, arr)
            arr.pop()
            return found, number

        return go(0, [])[1]


# leetcode submit region end(Prohibit modification and deletion)


class FindUniqueBinaryString(Solution):
    pass
