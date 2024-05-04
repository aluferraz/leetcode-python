from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        N = len(people)

        def go(left, right):
            if left > right:
                return 0
            if people[left] + people[right] <= limit:
                return 1 + go(left + 1, right - 1)
            else:
                return 1 + go(left, right - 1)

        return go(0, N - 1)


# leetcode submit region end(Prohibit modification and deletion)


class BoatsToSavePeople(Solution):
    pass
