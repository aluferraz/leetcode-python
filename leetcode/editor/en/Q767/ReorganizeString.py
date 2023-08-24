import collections
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = [0] * 26
        for c in s:
            letters[ord(c) - ord('a')] += 1
        pq = []

        for i in range(26):
            if letters[i] > 0:
                heapq.heappush(pq, (-letters[i], chr(i + ord('a'))))

        ans = collections.deque()
        N = len(s)
        while len(pq) > 0:
            cnt, c = heapq.heappop(pq)
            cnt = abs(cnt)
            if len(ans) > 0 and ans[-1] == c:
                if len(pq) > 0:
                    next_cnt, nextc = heapq.heappop(pq)
                    next_cnt = abs(next_cnt)
                    ans.append(nextc)
                    next_cnt -= 1
                    if next_cnt > 0:
                        heapq.heappush(pq, (-next_cnt, nextc))
                    heapq.heappush(pq, (-cnt, c))
                else:
                    if cnt == 1 and ans[0] != c:
                        ans.appendleft(c)
                    else:
                        return ""
            else:
                ans.append(c)
                cnt -= 1
                if cnt > 0:
                    heapq.heappush(pq, (-cnt, c))
        if len(ans) == N:
            return "".join(ans)
        return ""

    # leetcode submit region end(Prohibit modification and deletion)


class ReorganizeString(Solution):
    pass
