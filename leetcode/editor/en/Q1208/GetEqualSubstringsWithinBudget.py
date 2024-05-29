# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        left = 0
        right = 0
        ans = 0
        N = len(s)
        total_cost = 0
        while right < N:
            cost_here = abs(ord(s[right]) - ord(t[right]))
            total_cost += cost_here
            while total_cost > maxCost and left <= right:
                total_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, (right - left + 1))
            right += 1
        if ans == 0:
            return -1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class GetEqualSubstringsWithinBudget(Solution):
    pass
