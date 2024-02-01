from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        ans = [0] * N

        stack = []
        NGE = [i for i in range(N)]

        for i in range(N):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                NGE[stack.pop()] = i
            stack.append(i)

        for i in range(N):
            ans[i] = NGE[i] - i
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class DailyTemperatures(Solution):
    pass