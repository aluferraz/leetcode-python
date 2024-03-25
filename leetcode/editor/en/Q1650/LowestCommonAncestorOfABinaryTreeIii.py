from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def getLevel(node):
            level = 0
            current = node
            while current.parent is not None:
                level -= 1
                current = current.parent
            return abs(level)
        plevel = getLevel(p)
        qlevel = getLevel(q)

        def lca(a,b, alevel, blevel):
            if blevel > alevel:
                return lca(b,a,blevel,alevel)
            while alevel > blevel:
                a = a.parent
                alevel -= 1
            while a != b:
                a = a.parent
                b = b.parent
            return a

        return lca(p,q,plevel,qlevel)

        
# leetcode submit region end(Prohibit modification and deletion)


class LowestCommonAncestorOfABinaryTreeIii(Solution):
    pass