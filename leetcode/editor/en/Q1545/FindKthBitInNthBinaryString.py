# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ans = [0]
        for i in range(1, n):
            concat = [(x + 1) % 2 for x in reversed(ans)]
            ans.append(1)
            ans = ans + concat
        return ans
        # leetcode submit region end(Prohibit modification and deletion)


class FindKthBitInNthBinaryString(Solution):
    pass
