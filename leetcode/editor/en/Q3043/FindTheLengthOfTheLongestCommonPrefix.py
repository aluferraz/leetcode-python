from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie1 = {}
        trie2 = {}

        def add(s, root):
            current = root
            for c in s:
                if c not in current:
                    current[c] = {}
                current = current[c]

            current['*'] = {}

        for i in range(len(arr1)):
            add(str(arr1[i]), trie1)
        for i in range(len(arr2)):
            add(str(arr2[i]), trie2)

        def find(a, b):
            ans = 0
            for k in a.keys():
                if k == '*':
                    continue
                if k in b:
                    ans = max(ans, 1 + find(a[k], b[k]))
            return ans

        return find(trie1, trie2)


# leetcode submit region end(Prohibit modification and deletion)


class FindTheLengthOfTheLongestCommonPrefix(Solution):
    pass
