import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countPalindromePaths(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int
        """
        N = len(s)
        adj_list = collections.defaultdict(list)
        for i in range(N):
            adj_list[parent[i]].append((i, ord(s[i]) - ord('a')))

        total = 0
        counter = collections.Counter()

        def count(node, mask):
            nonlocal total

            total += counter[mask]
            for i in range(26):
                # when we XOR, every pair of letters cancels each other. so the xor reapeats every time we have the same string twice
                total += counter[mask ^ (1 << i)]
            counter[mask] += 1
            for next_node, next_letter in adj_list[node]:
                new_mask = (mask ^ (1 << next_letter))
                count(next_node, new_mask)

        count(0, 0)
        return total


# leetcode submit region end(Prohibit modification and deletion)


class CountPathsThatCanFormAPalindromeInATree(Solution):
    pass
