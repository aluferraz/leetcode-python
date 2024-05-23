from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        N = len(s)

        def is_palindrome(i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        ans = []

        def go(i, cur):
            if i == N:
                ans.append(list(cur))
                return
            for j in range(i, N):
                if is_palindrome(i, j):
                    cur.append(s[i:j + 1])
                    go(j + 1, cur)
                    cur.pop()

        go(0, [])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class PalindromePartitioning(Solution):
    pass
