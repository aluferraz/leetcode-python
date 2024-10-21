# leetcode submit region begin(Prohibit modification and deletion)
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        options = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(options)
        ans = []

        while len(options):
            qtd, lt = heapq.heappop(options)
            readd = []
            suffix = ""
            if len(ans) >= 2:
                suffix = "".join(ans[-2:])
            if suffix == "".join([lt, lt]):
                readd.append((qtd, lt))
                if len(options) == 0:
                    break
                qtd, lt = heapq.heappop(options)
            qtd = abs(qtd)
            if qtd > 0:
                ans.append(lt)
                qtd -= 1
                if qtd > 0:
                    readd.append((-qtd, lt))
            while readd:
                heapq.heappush(options, readd.pop())
        return "".join(ans)


# leetcode submit region end(Prohibit modification and deletion)


class LongestHappyString(Solution):
    pass
