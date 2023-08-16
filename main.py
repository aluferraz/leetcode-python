from contest import Solution
from leetcode.editor.en.Q1235.MaximumProfitInJobScheduling import MaximumProfitInJobScheduling
from leetcode.editor.en.Q490.TheMaze import TheMaze

dummy = Solution()
if __name__ == '__main__':
    print(TheMaze().hasPath(maze=[[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],
                            start=[0, 4], destination=[4, 4]))
