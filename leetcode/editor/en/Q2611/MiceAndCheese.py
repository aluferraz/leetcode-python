import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def miceAndCheese(self, reward1, reward2, k):
        """
        :type reward1: List[int]
        :type reward2: List[int]
        :type k: int
        :rtype: int
        """
        N = len(reward1)
        INF = 10 ** 20

        # cache = [
        #     ([None for _ in range(k + 1)]) for _ in range(N)
        # ]
        #
        # def go(i, k):
        #     if i == N:
        #         return -INF if k > 0 else 0
        #     if k == 0:
        #         cache[i][k] = sum(reward2[i::])
        #         return cache[i][k]
        #     if cache[i][k] is not None:
        #         return cache[i][k]
        #
        #     mouse_one = reward1[i] + go(i + 1, k - 1)
        #     mouse_two = reward2[i] + go(i + 1, k)
        #
        #     cache[i][k] = max(mouse_one, mouse_two)
        #     return cache[i][k]
        #
        # return go(0, k)

        best_r1 = []

        for i in range(N):
            best_r1.append((reward1[i] - reward2[i], i))

        best_r1.sort()
        ans = 0
        mask = 0
        for i in range(k):
            _, idx = best_r1[N - 1 - i]
            ans += reward1[idx]
            mask |= (1 << idx)
        for i in range(N):
            if mask & (1 << i) == 0:
                ans += reward2[i]
        return ans

    # leetcode submit region end(Prohibit modification and deletion)


class MiceAndCheese(Solution):
    pass
