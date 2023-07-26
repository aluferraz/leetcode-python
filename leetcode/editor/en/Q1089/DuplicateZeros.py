import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        N = len(arr)
        stack = collections.deque()

        for i in range(N - 1, -1, -1):
            stack.append(arr[i])
            if arr[i] == 0:
                stack.popleft()
                stack.append(0)

        for i in range(N):
            arr[i] = stack[i]
        arr.reverse()


        # leetcode submit region end(Prohibit modification and deletion)


class DuplicateZeros(Solution):
    pass
