# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSwaps(self, s: str) -> int:
        open = []
        for c in s:
            if c == '[':
                open.append(c)
            else:
                if len(open) != 0:
                    open.pop()
        return len(open) // 2 if len(open) % 2 == 0 else (len(open) + 1) // 2


# leetcode submit region end(Prohibit modification and deletion)


class MinimumNumberOfSwapsToMakeTheStringBalanced(Solution):
    pass
