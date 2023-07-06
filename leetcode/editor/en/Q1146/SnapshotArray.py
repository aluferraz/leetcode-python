import bisect
import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.snap_id = 0
        self.snaps = {
            k: {0: 0} for k in range(length)
        }
        self.snapsIndex = [
            [0] for _ in range(length)
        ]

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.snaps[index][self.snap_id] = val
        lastSeen = self.snapsIndex[index]
        if self.snap_id > lastSeen[len(lastSeen) - 1]:
            lastSeen.append(self.snap_id)

    def snap(self):
        """
        :rtype: int
        """
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """

        def find(snapId, arr):
            left = 0
            right = len(arr) - 1
            ans = 0
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == snapId:
                    return arr[mid]
                if arr[mid] < snapId:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return arr[ans]

        lastModifIdx = find(snap_id, self.snapsIndex[index])

        return self.snaps[index][lastModifIdx]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# leetcode submit region end(Prohibit modification and deletion)
