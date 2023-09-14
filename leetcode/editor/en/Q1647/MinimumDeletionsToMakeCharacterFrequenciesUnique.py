import collections
import heapq
from typing import List

import sortedcontainers


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """

        counter = [0] * 26
        frequencies = collections.defaultdict(int)
        for c in s:
            counter[ord(c) - ord('a')] += 1
        for repeat in counter:
            if repeat > 0:
                frequencies[repeat] += 1

        must_be_deleted = []

        for repeat, occurrences in frequencies.items():
            if occurrences > 1:
                must_be_deleted.append((-repeat))
        heapq.heapify(must_be_deleted)
        ans = 0
        while len(must_be_deleted) > 0:
            repeat = heapq.heappop(must_be_deleted)
            repeat = abs(repeat)
            occurrence = frequencies[repeat]
            if occurrence <= 1:
                continue
            frequencies[repeat] = 1
            frequencies[repeat - 1] += (occurrence - 1)
            if frequencies[repeat - 1] > 1 and repeat - 1 > 0:
                heapq.heappush(must_be_deleted, -(repeat - 1))

            ans += (occurrence - 1)

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MinimumDeletionsToMakeCharacterFrequenciesUnique(Solution):
    pass
