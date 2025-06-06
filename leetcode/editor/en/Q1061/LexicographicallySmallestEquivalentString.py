# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [-1] * 26
        N = min(len(s1), len(s2))

        def find(i):
            while parent[i] >= 0:
                i = parent[i]
            return i

        def union(i, j):
            if i == j:
                return
            if j < i:  # lexicographically smaller
                return union(find(j), find(i))
            parent[i] += parent[j]
            parent[j] = i

        for i in range(N):
            c1 = ord(s1[i]) - ord('a')
            c2 = ord(s2[i]) - ord('a')
            union(find(c1), find(c2))
        ans = []
        for i in range(len(baseStr)):
            c1 = ord(baseStr[i]) - ord('a')
            ans.append(chr(find(c1) + ord('a')))
        return "".join(ans)


# leetcode submit region end(Prohibit modification and deletion)


class LexicographicallySmallestEquivalentString(Solution):
    pass
