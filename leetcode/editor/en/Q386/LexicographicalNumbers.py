from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [[] for _ in range(n)]

        for i in range(n):
            str_num = str(i)
            idx = int(str_num[0]) - 1
            ans[idx].append(str_num)
        return "".join("".join(x) for x in ans)


# leetcode submit region end(Prohibit modification and deletion)


class LexicographicalNumbers(Solution):
    pass
