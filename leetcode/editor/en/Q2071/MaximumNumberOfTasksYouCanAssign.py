from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:

        N = len(tasks)
        M = len(workers)
        left = 0
        right = N + 1
        ans = 0
        tasks.sort()
        workers.sort()
        INF = 10 ** 20

        def go(i, j, target):
            if i == target:
                return 0, 0
            if j == M:
                return INF, 0

            if workers[j] >= tasks[i]:
                used, completed = go(i + 1, j + 1, target)
                return used, completed + 1
            else:
                if workers[j] + strength >= tasks[i]:
                    used_taking, completed_taking = go(i + 1, j + 1, target)
                    used_taking += 1
                    completed_taking += 1
                    used_skipping, completed_skipping = go(i, j + 1, target)
                    used_ignoring, completed_ignoring = go(i + 1, j, target)
                    options = [(used_taking, -completed_taking), (used_skipping, -completed_skipping),
                               (used_ignoring, -completed_ignoring)]
                    options.sort()
                    ans_here = options[0]
                    return ans_here[0], abs(ans_here[1])

            return INF

        def good(target):
            min_pills = go(0, 0, target)
            return min_pills < pills

        while left < right:
            mid = (left + right) // 2
            if good(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MaximumNumberOfTasksYouCanAssign(Solution):
    pass
