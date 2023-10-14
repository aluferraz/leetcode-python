from contest import Solution
from leetcode.editor.en.Q2009.MinimumNumberOfOperationsToMakeArrayContinuous import \
    MinimumNumberOfOperationsToMakeArrayContinuous
from leetcode.editor.en.Q2251.NumberOfFlowersInFullBloom import NumberOfFlowersInFullBloom
from leetcode.editor.en.Q505.TheMazeIi import TheMazeIi

dummy = Solution()

if __name__ == '__main__':
    # print(BuildArrayWhereYouCanFindTheMaximumExactlyKComparisons().numOfArrays(n=50, m=100, k=25))
    print(
        TheMazeIi().shortestDistance(
            maze=[[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], start=[0, 4],
            destination=[4, 4]
        ))
