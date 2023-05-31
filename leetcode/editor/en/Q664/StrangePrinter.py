import collections
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def strangePrinter(self, s):
        cache = collections.defaultdict(lambda: None)
        n = len(s)
        def calc(left, right):
            key = (left, right)
            if cache[key] != None:
                return cache[key]
            original = s[right]
            breakpos = -1
            ans = n
            for i in range(left, right):
                if s[i] != original and breakpos == -1:
                    breakpos = i
                if breakpos != -1:
                    ansHere = 1 + calc(breakpos, i) + calc(i + 1, right)
                    ans = min(ansHere, ans)
            if breakpos == -1:
                ans = 0
            cache[key] = ans
            return ans

        return calc(0, len(s) - 1) + 1

        # leetcode submit region end(Prohibit modification and deletion)


class StrangePrinter(Solution):
    pass
