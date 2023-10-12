from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        """
        :type flowers: List[List[int]]
        :type people: List[int]
        :rtype: List[int]
        """
        START = 1
        END = -1
        VISIT = 2

        timeline = []

        for s, e in flowers:
            timeline.append((s, START, -1))
            timeline.append((e + 1, END, -1))

        for i in range(len(people)):
            p = people[i]
            timeline.append((p, VISIT, i))

        timeline.sort()

        flowers = 0
        N = len(timeline)
        ans = [-1] * len(people)
        for i in range(N):
            t, e, a = timeline[i]
            if e == START:
                flowers += 1
            elif e == END:
                flowers -= 1
            else:
                ans[a] = flowers
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfFlowersInFullBloom(Solution):
    pass
