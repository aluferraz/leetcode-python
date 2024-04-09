import collections
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = collections.Counter(students)
        sandwiches.reverse()

        while len(sandwiches) > 0:
            target = sandwiches.pop()
            if cnt[target] > 0:
                cnt[target] -= 1
            else:
                sandwiches.append(target)
                break
        return sum(cnt.values())
# leetcode submit region end(Prohibit modification and deletion)


class NumberOfStudentsUnableToEatLunch(Solution):
    pass