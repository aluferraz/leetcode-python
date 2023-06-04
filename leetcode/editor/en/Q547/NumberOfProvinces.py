# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        N = len(isConnected)
        parents = [-1 for _ in range(N)]

        def union(i, j):
            if i == j:
                return
            if parents[j] < parents[i]:
                return union(j, i)
            parents[i] += parents[j]
            parents[j] = i

        def find(i):
            path_comp = []
            while parents[i] >= 0:
                path_comp.append(i)
                i = parents[i]
            while len(path_comp) > 0:
                parents[path_comp.pop()] = i
            return i

        for i in range(N):
            for j in range(N):
                # print(isConnected[i][j])
                if isConnected[i][j] == 1:
                    union(find(i), find(j))

        ans = 0
        for comp in parents:
            if comp < 0:
                ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfProvinces(Solution):
    pass
