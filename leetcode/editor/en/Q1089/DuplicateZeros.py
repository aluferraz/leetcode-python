import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        N = len(arr)
        zeros_indexes = []
        for i in range(N):
            if arr[i] == 0:
                if i + 1 < N:
                    zeros_indexes.append(i + 1)
        if len(zeros_indexes) == 0:
            return

        tail_pos = N - 1
        for i in range(N - 1 - len(zeros_indexes), -1, -1):
            arr[tail_pos] = arr[i]
            tail_pos -= 1
            if arr[i] == 0:
                arr[tail_pos] = 0
                tail_pos -= 1

    # leetcode submit region end(Prohibit modification and deletion)


class DuplicateZeros(Solution):
    pass
