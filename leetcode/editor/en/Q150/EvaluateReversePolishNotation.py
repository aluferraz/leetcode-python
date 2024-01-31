import math
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        expression = []

        for t in tokens:
            if t in {'/','*','+', '-'}:
                a = expression.pop()
                b = expression.pop()
                if t == '/':
                    res = b / a
                    expression.append(math.floor(res) if res >= 0 else math.ceil(res))
                elif t == '*':
                    expression.append(a * b)
                elif t == '+':
                    expression.append(a + b)
                elif t == '-':
                    expression.append(a - b)
            else:
                expression.append(int(t))
        return expression.pop()
# leetcode submit region end(Prohibit modification and deletion)


class EvaluateReversePolishNotation(Solution):
    pass