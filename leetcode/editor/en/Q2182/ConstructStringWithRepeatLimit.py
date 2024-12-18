import collections
import heapq
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        cnt = collections.Counter(s)
        cnt = [(-(ord(c) - ord('a')), -t) for c, t in cnt.items()]
        heapq.heapify(cnt)

        ans = []
        cant_repeat = ""
        bkp = []
        while cnt:
            c,tot = heapq.heappop(cnt)
            if c == cant_repeat:
                bkp.append( (c, tot))
                if cnt:
                    c, tot = heapq.heappop(cnt)
                else:
                    break
            tot = abs(tot)
            shouldUse = 10 ** 20
            if bkp:
                shouldUse = 1
            for _ in range(min(tot, repeatLimit,shouldUse)):
                ans.append(c)
            tot -= min(tot, repeatLimit,shouldUse)
            cant_repeat = c
            if tot > 0:
                bkp.append((c,-tot))
            while bkp:
                heapq.heappush(cnt, bkp.pop())
        ans_s = []
        for asc in ans:
            ans_s.append(chr(abs(asc) + ord('a')))
        return "".join(ans_s)



        
# leetcode submit region end(Prohibit modification and deletion)


class ConstructStringWithRepeatLimit(Solution):
    pass
    