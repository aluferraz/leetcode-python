from contest import Solution
from leetcode.editor.en.Q2845.CountOfInterestingSubarrays import CountOfInterestingSubarrays
from leetcode.editor.en.Q2846.MinimumEdgeWeightEquilibriumQueriesInATree import \
    MinimumEdgeWeightEquilibriumQueriesInATree

dummy = Solution()
if __name__ == '__main__':
    print(MinimumEdgeWeightEquilibriumQueriesInATree().minOperationsQueries(n=7, edges=[[0, 1, 1], [1, 2, 1], [2, 3, 1],
                                                                                        [3, 4, 2], [4, 5, 2],
                                                                                        [5, 6, 2]],
                                                                            queries=[[0, 3], [3, 6], [2, 6], [0, 6]]))
