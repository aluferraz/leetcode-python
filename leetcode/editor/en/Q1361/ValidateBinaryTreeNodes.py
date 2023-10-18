import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def validateBinaryTreeNodes(self, N, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        if N == 1:
            return leftChild[0] == rightChild[0] == -1
        visited = [0] * N
        parents = [-1] * N

        def find(i):
            while parents[i] >= 0:
                i = parents[i]
            return i

        def union(a, b):
            i, j = find(a), find(b)
            if i == j:
                return False
            if parents[j] < parents[i]:
                return union(b, a)
            parents[i] += parents[j]
            parents[j] = i
            return True


        for i in range(N):
            if leftChild[i] != -1:
                visited[leftChild[i]] += 1
                if not union(i, leftChild[i]):
                    return False
            if rightChild[i] != -1:
                visited[rightChild[i]] += 1
                if not union(i, rightChild[i]):
                    return False

        return max(visited) == 1 and abs(min(parents)) == N


# leetcode submit region end(Prohibit modification and deletion)


class ValidateBinaryTreeNodes(Solution):
    pass
