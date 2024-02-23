from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        cnt = [0] * (n+1)
        cnt1 = [0] * (n+1)
        for a,b in trust:
            cnt[b] += 1
            cnt1[a] += 1
        for i in range(1,n +1 ):
            if cnt[i] == n-1 and cnt1[i] == 0 :
                return i
        return -1


# leetcode submit region end(Prohibit modification and deletion)


class FindTheTownJudge(Solution):
    pass