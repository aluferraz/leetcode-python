import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = {'#': {}}

        def buildTrie(s):
            current = root['#']
            for c in s:
                if c in current:
                    current = current[c]
                else:
                    current[c] = {}
                    current = current[c]
            if '*' in current:
                heapq.heappush(current['*'], (len(s), s))
            else:
                current['*'] = [(len(s), s)]

        def getShortest(s):
            current = root['#']
            for c in s:
                if c in current:
                    current = current[c]
                else:
                    return s
                if '*' in current:
                    _, shorter = current['*'][0]
                    return shorter
            return s

        for w in dictionary:
            buildTrie(w)

        ans = sentence.split(' ')
        N = len(ans)

        for i in range(N):
            ans[i] = getShortest(ans[i])
        return " ".join(ans)


# leetcode submit region end(Prohibit modification and deletion)


class ReplaceWords(Solution):
    pass
