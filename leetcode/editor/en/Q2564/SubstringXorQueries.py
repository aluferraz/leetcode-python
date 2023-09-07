import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def substringXorQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[List[int]]
        """

        numbers = collections.defaultdict(lambda: list([-1, -1]))
        N = len(s)
        for l in range(min(33, N)):
            for i in range(N - l):
                num = int(s[i:i + l + 1], 2)
                if num not in numbers:
                    numbers[num] = [i, i + l]
        ans = []
        for q in queries:
            target = (q[1] ^ q[0])
            ans.append(numbers[target])
        return ans

    # leetcode submit region end(Prohibit modification and deletion)


class SubstringXorQueries(Solution):
    pass
