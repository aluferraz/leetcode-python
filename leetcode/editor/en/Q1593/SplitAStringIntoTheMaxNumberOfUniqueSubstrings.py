# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        N = len(s)

        def go(i, existing):
            if i == N:
                return True, len(existing)
            s_here = []
            ans_here = -(10 ** 20)
            valid = False
            for j in range(i, N):
                s_here.append(s[j])
                str_here = "".join(s_here)
                if str_here not in existing:
                    existing.add(str_here)
                    valid, res = go(j + 1, existing)
                    if valid:
                        ans_here = max(ans_here, res)
                        valid = True
                    existing.remove(str_here)
            return valid, ans_here

        return go(0, set())[1]


# leetcode submit region end(Prohibit modification and deletion)


class SplitAStringIntoTheMaxNumberOfUniqueSubstrings(Solution):
    pass
