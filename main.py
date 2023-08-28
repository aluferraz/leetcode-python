from contest import Solution
from leetcode.editor.en.Q2818.ApplyOperationsToMaximizeScore import ApplyOperationsToMaximizeScore
from leetcode.editor.en.Q2835.MinimumOperationsToFormSubsequenceWithTargetSum import \
    MinimumOperationsToFormSubsequenceWithTargetSum
from leetcode.editor.en.Q403.FrogJump import FrogJump

dummy = Solution()
if __name__ == '__main__':
    print(MinimumOperationsToFormSubsequenceWithTargetSum().minOperations([128, 1, 128, 1, 64],
                                                                          4))  # 4
    print(MinimumOperationsToFormSubsequenceWithTargetSum().minOperations([16, 16, 4],
                                   3))  # 2
    print(MinimumOperationsToFormSubsequenceWithTargetSum().minOperations([2, 32, 32, 32, 2, 1],
                                   7))  # 3
    print(MinimumOperationsToFormSubsequenceWithTargetSum().minOperations([1, 2, 8],
                                   7))  # 1
