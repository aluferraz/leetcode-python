from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        cur = head
        while cur is not None:
            arr.append(cur.val)
            cur = cur.next
        N = len(arr)
        left = 0
        right = N-1
        while left <= right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return True
# leetcode submit region end(Prohibit modification and deletion)


class PalindromeLinkedList(Solution):
    pass