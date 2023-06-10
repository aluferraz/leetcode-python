from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        N = len(letters)
        left = 0
        right = N
        while left < right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return letters[left % N]

    # leetcode submit region end(Prohibit modification and deletion)


class FindSmallestLetterGreaterThanTarget(Solution):
    pass
