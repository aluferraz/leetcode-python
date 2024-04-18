import collections
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        ans = [26] * 8501

        def compare_lists(a,b):
            for i in range(min(len(a),len(b))):
                if a[i] < b[i]:
                    return a
                if b[i] < a[i]:
                    return b
            if len(a) < len(b):
                return a
            if len(b) < len(a):
                return b
            return b

        def go(node, word):
            nonlocal ans
            if node is None:
                return
            word.appendleft(node.val)
            if node.left is None and node.right is None:
                ans = list(compare_lists(ans, word))
            else:
                go(node.left, word)
                go(node.right, word)
            word.popleft()

        go(root, collections.deque())

        return "".join([chr(ans[i] + ord('a')) for i in range(len(ans))])

        
# leetcode submit region end(Prohibit modification and deletion)


class SmallestStringStartingFromLeaf(Solution):
    pass