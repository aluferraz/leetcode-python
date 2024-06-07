import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        cnt = collections.OrderedDict()
        hand.sort()
        for h in hand:
            if h in cnt:
                cnt[h] += 1
            else:
                cnt[h] = 1
        while len(cnt) > 0:
            group = []
            items = list(cnt.items())
            if len(items) < groupSize:
                return False
            for d, c in items:
                if len(group) == 0:
                    group.append(d)
                else:
                    if d != (group[-1] + 1):
                        return False
                    group.append(d)
                cnt[d] -= 1
                if cnt[d] == 0:
                    cnt.pop(d)
                if len(group) == groupSize:
                    break
        return True


# leetcode submit region end(Prohibit modification and deletion)


class HandOfStraights(Solution):
    pass
