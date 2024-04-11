import collections
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        def next_greater_element(arr):
            NGE = [len(arr)] * len(arr)
            stack = []
            for i in range(len(arr)):
                while len(stack) > 0 and arr[i] > arr[stack[-1]]:
                    NGE[stack.pop()] = i
                stack.append(i)
            return NGE

        NGE = next_greater_element(preorder)
        N = len(preorder)
        min_seen = preorder[0]
        boundary = [None] * (N + 1)
        boundary[0] = min(preorder)
        for i in range(N):
            #no number to the right of NGE[i] can be less than min_seen
            min_seen = min(min_seen, preorder[i])
            boundary[NGE[i]] = min_seen
            if boundary[i] is None:
                boundary[i] = boundary[i-1]
            if preorder[i] < boundary[i]:
                return False
        return True














# leetcode submit region end(Prohibit modification and deletion)


class VerifyPreorderSequenceInBinarySearchTree(Solution):
    pass