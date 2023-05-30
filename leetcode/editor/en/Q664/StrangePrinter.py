import collections
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = collections.defaultdict(int)
        for i in range(0, len(s)):
            counter[s[i]] += 1
        pq = []
        for letter in counter:
            heapq.heappush(pq, (counter[letter], letter))

        while len(pq) > 0:
            print(heapq.heappop(pq))


# leetcode submit region end(Prohibit modification and deletion)


class StrangePrinter(Solution):
    pass
