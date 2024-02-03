from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        N = len(str(high))
        current = ['0'] * N

        def go(i, prev, began):
            if i == N:
                num = int("".join(current))
                if num >= low and num <= high:
                    ans.append(num)
                return
            if prev == 9:
                return
            if not began:
                go(i+1, 0, began)
                for j in range(1,10):
                    current[i] = str(j)
                    go(i + 1, j, True)
            else:
                current[i] = str(prev+1)
                go(i + 1, prev+1, began)

        go(0, -1, False)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class SequentialDigits(Solution):
    pass