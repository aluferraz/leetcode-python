from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def go(node, arr):
            if node is None:
                return arr
            for c in node.children:
                go(c, arr)
            arr.append(node.val)
            return arr

        return go(root, [])


# leetcode submit region end(Prohibit modification and deletion)


class NAryTreePostorderTraversal(Solution):
    pass
