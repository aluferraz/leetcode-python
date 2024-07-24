from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [x[1] for x in sorted(zip(heights, names), reverse=True)]


# leetcode submit region end(Prohibit modification and deletion)


class SortThePeople(Solution):
    pass
