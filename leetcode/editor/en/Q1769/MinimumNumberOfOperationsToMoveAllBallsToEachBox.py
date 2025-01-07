from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)
        ans = [0] * N
        for i in range(N):
            for j in range(i + 1, N):
                if boxes[j]:
                    ans[i] += (j - i)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MinimumNumberOfOperationsToMoveAllBallsToEachBox(Solution):
    pass
