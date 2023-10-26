from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # the pattern repeats itself but inversing

        def find(level, k, inverted):
            if level == 1:
                return 0 if not inverted else 1
            level_elements = 2 ** (level - 1)
            previous_level_elements = level_elements // 2
            if k > previous_level_elements:
                return find(level - 1, k - previous_level_elements, not inverted)
            return find(level - 1, k, inverted)

        return find(n, k, False)


# leetcode submit region end(Prohibit modification and deletion)


class KThSymbolInGrammar(Solution):
    pass
