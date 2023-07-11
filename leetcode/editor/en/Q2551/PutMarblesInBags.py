import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)

class SegmentTree(object):

    def __init__(self, arr, comparator):
        N = len(arr)
        self.N = N
        self.tree = [(0, 0) for _ in range(2 * N)]
        for i in range(N, 2 * N):
            self.tree[i] = arr[i - N]
        for i in range(N - 1, -1, -1):
            first = self.tree[2 * i]
            second = self.tree[(2 * i) + 1]
            self.tree[i] = comparator(first, second)
        self.comparator = comparator

    def query(self, left, right):
        left += self.N
        right += self.N
        ans = None if left != right else self.tree[left]
        while left < right:
            if left % 2 == 1:
                if ans is None:
                    ans = self.tree[left]
                else:
                    ans = self.comparator(ans, self.tree[left])

                left += 1
            if right % 2 == 1:
                right -= 1
                if ans is None:
                    ans = self.tree[right]
                else:
                    ans = self.comparator(ans, self.tree[right])

            left //= 2
            right //= 2
        return ans


class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """

        scores = []
        for (x, y) in zip(weights, weights[1:]):
            scores.append(x + y)
        scores.sort()

        mini = sum(scores[:k - 1])
        maxi = sum(scores[len(scores) - k + 1:])

        return maxi - mini


# leetcode submit region end(Prohibit modification and deletion)


class PutMarblesInBags(Solution):
    pass
