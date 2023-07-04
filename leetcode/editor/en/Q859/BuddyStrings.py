# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        N = len(s)
        M = len(goal)

        s = [c for c in s]
        if N != M:
            return False

        first_diff = -1
        second_diff = -1
        maxCounter = [0 for _ in range(26)]

        for i in range(N):
            if s[i] != goal[i]:
                if first_diff == -1:
                    first_diff = i
                else:
                    second_diff = i

            maxCounter[ord(s[i]) - ord('a')] += 1
        if first_diff == second_diff:
            return max(maxCounter) > 1
        if second_diff == -1:
            return False

        temp = s[first_diff]
        s[first_diff] = s[second_diff]
        s[second_diff] = temp

        return "".join(s) == goal


# leetcode submit region end(Prohibit modification and deletion)


class BuddyStrings(Solution):
    pass
