# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        tot = bin(num2).count('1')
        num1 = f"{num1:032b}"
        ans = list(num1)
        free = []
        for i in range(32):
            if tot == 0:
                ans[i] = '0'
                free.append(i)
            elif ans[i] == '1':
                tot -= 1
            else:
                free.append(i)
        for i in range(tot):
            ans[free.pop()] = '1'
        return int("".join(ans), 2)


# leetcode submit region end(Prohibit modification and deletion)


class MinimizeXor(Solution):
    pass
