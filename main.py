from contest import Solution
from leetcode.editor.en.Q1743.RestoreTheArrayFromAdjacentPairs import RestoreTheArrayFromAdjacentPairs
from leetcode.editor.en.Q2642.DesignGraphWithShortestPathCalculator import DesignGraphWithShortestPathCalculator
from leetcode.editor.en.Q815.BusRoutes import BusRoutes

dummy = Solution()

if __name__ == '__main__':
    # print(RestoreTheArrayFromAdjacentPairs().restoreArray([[2,1],[3,4],[3,2]]))
    print(BusRoutes().numBusesToDestination(
        [[10, 13, 22, 28, 32, 35, 43], [2, 11, 15, 25, 27], [6, 13, 18, 25, 42], [5, 6, 20, 27, 37, 47],
         [7, 11, 19, 23, 35], [7, 11, 17, 25, 31, 43, 46, 48], [1, 4, 10, 16, 25, 26, 46], [7, 11],
         [3, 9, 19, 20, 21, 24, 32, 45, 46, 49], [11, 41]],
        37, 43
    ))
