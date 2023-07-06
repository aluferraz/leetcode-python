import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """

        children = [0 for _ in range(k)]
        N = len(cookies)
        INF = 10 ** 20
        cookies.sort()

        cache = {}

        def distribute(i, min_child, max_child):
            if i == N:
                return max_child

            # if (i, min_child, max_child) in cache:
            #     return cache[(i, min_child, max_child)]

            best = INF

            for j in range(k):
                children[j] += cookies[i]

                ansHere = distribute(i + 1, min(children), max(children))
                best = min(best, ansHere)
                children[j] -= cookies[i]

            cache[(i, min_child, max_child)] = best
            return best

        ans = distribute(0, 0, 0)

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class FairDistributionOfCookies(Solution):
    pass
