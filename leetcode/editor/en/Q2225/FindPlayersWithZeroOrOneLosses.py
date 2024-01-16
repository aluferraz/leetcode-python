from typing import List, Optional
import collections
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        seen = set()
        lost_count = collections.defaultdict(int)

        for match in matches:
            w,l = match
            lost_count[l] += 1
            seen.add(w)
            seen.add(l)

        never_lost = []
        one_lost = []
        seen = sorted(seen)

        for p in seen:
            if lost_count[p] == 1:
                one_lost.append(p)
            elif lost_count[p] == 0:
                never_lost.append(p)
        return [never_lost,one_lost]

# leetcode submit region end(Prohibit modification and deletion)


class FindPlayersWithZeroOrOneLosses(Solution):
    pass