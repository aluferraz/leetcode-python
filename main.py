from contest import Solution
from leetcode.editor.en.Q1146.SnapshotArray import SnapshotArray
from leetcode.editor.en.Q1150.CheckIfANumberIsMajorityElementInASortedArray import \
    CheckIfANumberIsMajorityElementInASortedArray
from leetcode.editor.en.Q1802.MaximumValueAtAGivenIndexInABoundedArray import MaximumValueAtAGivenIndexInABoundedArray
from leetcode.editor.en.Q69.Sqrtx import Sqrtx
from leetcode.editor.en.Q808.SoupServings import SoupServings

if __name__ == '__main__':
    snapshotArr = SnapshotArray(4)
    snapshotArr.snap()
    snapshotArr.snap()
    snapshotArr.get(3, 1)
    snapshotArr.set(2, 4)
    snapshotArr.snap()
    snapshotArr.set(1, 4)
