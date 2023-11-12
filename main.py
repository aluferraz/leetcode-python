from contest import Solution
from leetcode.editor.en.Q1743.RestoreTheArrayFromAdjacentPairs import RestoreTheArrayFromAdjacentPairs
from leetcode.editor.en.Q2642.DesignGraphWithShortestPathCalculator import DesignGraphWithShortestPathCalculator

dummy = Solution()

if __name__ == '__main__':
    # print(RestoreTheArrayFromAdjacentPairs().restoreArray([[2,1],[3,4],[3,2]]))

    obj = DesignGraphWithShortestPathCalculator(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
    obj.shortestPath(3, 2)
    obj.shortestPath(0, 3)
    obj.addEdge([1, 3, 4])
    obj.shortestPath(0, 3)
