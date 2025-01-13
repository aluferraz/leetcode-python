# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        def good(s, locked, opener):
            opened = 0
            unlocked = 0
            for char, lock in zip(s, locked):
                if lock == "0":
                    unlocked += 1
                elif char == opener:
                    opened += 1
                elif opened > 0:
                    opened -= 1
                elif unlocked > 0:
                    unlocked -= 1
                else:
                    return False
            return (opened - unlocked) % 2 == 0

        return good(s, locked, "(") and good(s[::-1], locked[::-1], ")")


# leetcode submit region end(Prohibit modification and deletion)


class CheckIfAParenthesesStringCanBeValid(Solution):
    pass
