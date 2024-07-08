# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        left = 0
        right = 0
        seen = set()
        N = len(s)
        ans = N
        while right < N:
            c = s[right]
            length = 0
            if c in seen:
                length = right - left
                ans += (length * (length + 1) // 2) - length
            while c in seen:
                seen.remove(s[left])
                left += 1

            seen.add(c)
            right += 1
        length = right - left
        ans += (length * (length + 1) // 2) - length
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class CountSubstringsWithoutRepeatingCharacter(Solution):
    pass
