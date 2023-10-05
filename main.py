from contest import Solution
from leetcode.editor.en.Q1512.NumberOfGoodPairs import NumberOfGoodPairs
from leetcode.editor.en.Q1804.ImplementTrieIiPrefixTree import ImplementTrieIiPrefixTree
from leetcode.editor.en.Q2038.RemoveColoredPiecesIfBothNeighborsAreTheSameColor import \
    RemoveColoredPiecesIfBothNeighborsAreTheSameColor
from leetcode.editor.en.Q2393.CountStrictlyIncreasingSubarrays import CountStrictlyIncreasingSubarrays
from leetcode.editor.en.Q2871.SplitArrayIntoMaximumNumberOfSubarrays import SplitArrayIntoMaximumNumberOfSubarrays
from leetcode.editor.en.Q456.One32Pattern import One32Pattern

dummy = Solution()

if __name__ == '__main__':
    obj = ImplementTrieIiPrefixTree()
    obj.insert("apple")
    obj.insert("apple")
    param_2 = obj.countWordsEqualTo("apple")
    param_3 = obj.countWordsStartingWith("app")
    obj.erase("apple")
    obj.countWordsEqualTo("apple")
    param_3 = obj.countWordsStartingWith("app")
    obj.erase("apple")
    obj.countWordsEqualTo("apple")
