from contest import Solution
from leetcode.editor.en.Q1483.KthAncestorOfATreeNode import TreeAncestor
from leetcode.editor.en.Q2818.ApplyOperationsToMaximizeScore import ApplyOperationsToMaximizeScore
from leetcode.editor.en.Q2835.MinimumOperationsToFormSubsequenceWithTargetSum import \
    MinimumOperationsToFormSubsequenceWithTargetSum
from leetcode.editor.en.Q403.FrogJump import FrogJump

dummy = Solution()
if __name__ == '__main__':
    ta = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
    print(ta.getKthAncestor(3, 1))
    print(ta.getKthAncestor(5, 2))
    print(ta.getKthAncestor(6, 3))
