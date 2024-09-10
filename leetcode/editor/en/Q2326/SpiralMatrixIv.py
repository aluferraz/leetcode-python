from typing import List, Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1 for _ in range(n)] for _ in range(m)]
        if head is None:
            return ans
        DIRECTIONS = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        ]

        def is_valid_idx(i, j):
            return i >= 0 and i < m and j >= 0 and j < n and ans[i][j] == -1

        def go(i, j, dir, current):
            if current is None:
                return True
            if not is_valid_idx(i, j):
                return False
            ans[i][j] = current.val
            dy, dx = DIRECTIONS[dir]
            valid = go(i + dy, j + dx, dir, current.next)
            while not valid:
                dir = (dir + 1) % (len(DIRECTIONS))
                dy, dx = DIRECTIONS[dir]
                valid = go(i + dy, j + dx, dir, current.next)
            return valid

        go(0, 0, 0, head)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class SpiralMatrixIv(Solution):
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ll = ListNode(-1)
        current = ll
        for c in head:
            current.next = ListNode(c)
            current = current.next
        return super().spiralMatrix(m, n, ll.next)
