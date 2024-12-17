from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        inbound = [0] * n

        for u, v in edges:
            inbound[v] += 1

        if inbound.count(0) > 1:
            return -1
        for i in range(n):
            if inbound[i] == 0:
                return i
        return -1


# leetcode submit region end(Prohibit modification and deletion)


class FindChampionIi(Solution):
    pass
