from contest import Solution
from leetcode.editor.en.Q1347.MinimumNumberOfStepsToMakeTwoStringsAnagram import \
    MinimumNumberOfStepsToMakeTwoStringsAnagram
from leetcode.editor.en.Q1657.DetermineIfTwoStringsAreClose import DetermineIfTwoStringsAreClose
from leetcode.editor.en.Q300.LongestIncreasingSubsequence import LongestIncreasingSubsequence
from leetcode.editor.en.Q380.InsertDeleteGetrandomO1 import InsertDeleteGetrandomO1
from leetcode.editor.en.Q446.ArithmeticSlicesIiSubsequence import ArithmeticSlicesIiSubsequence

dummy = Solution()

if __name__ == '__main__':
    obj = InsertDeleteGetrandomO1()
    obj.insert(0)
    obj.insert(1)
    obj.remove(0)
    obj.insert(2)
    obj.remove(1)
    print(obj.getRandom())
