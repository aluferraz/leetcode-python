from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        stack = []
        target.reverse()
        ans = []
        for i in range(1, n + 1):
            while len(stack) > 0 and stack[-1] < target[-1]:
                ans.append("Pop")
                stack.pop()

            ans.append("Push")
            stack.append(i)
            if stack[-1] == target[-1]:
                target.pop()
                stack.append(10 ** 20)  # stop marker
            if len(target) == 0:
                break

        return ans
    # leetcode submit region end(Prohibit modification and deletion)


class BuildAnArrayWithStackOperations(Solution):
    pass
