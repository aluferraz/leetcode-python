from contest import Solution
from leetcode.editor.en.Q1658.MinimumOperationsToReduceXToZero import MinimumOperationsToReduceXToZero
from leetcode.editor.en.Q2670.FindTheDistinctDifferenceArray import FindTheDistinctDifferenceArray
from leetcode.editor.en.Q2672.NumberOfAdjacentElementsWithTheSameColor import NumberOfAdjacentElementsWithTheSameColor
from leetcode.editor.en.Q2861.MaximumNumberOfAlloys import MaximumNumberOfAlloys
from leetcode.editor.en.Q2862.MaximumElementSumOfACompleteSubsetOfIndices import \
    MaximumElementSumOfACompleteSubsetOfIndices

dummy = Solution()

if __name__ == '__main__':
    print(
        NumberOfAdjacentElementsWithTheSameColor().colorTheArray(N=4,
                                                                 queries=[[0, 2], [1, 2], [3, 1], [1, 1], [2, 1]]
                                                                 ))
