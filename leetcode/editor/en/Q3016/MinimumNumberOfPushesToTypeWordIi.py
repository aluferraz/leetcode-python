# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def minimumPushes(self, word: str) -> int:
        letters = collections.Counter(word)
        letters_sorted = sorted([(-cnt, l) for (l, cnt) in letters.items()])
        lmap = {
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
        }
        cost = [0] * 26
        lkeys = list(lmap.keys())
        lidx = 0

        for _, l in letters_sorted:
            lmap[lkeys[lidx]].append(l)
            cost[ord(l) - ord('a')] = len(lmap[lkeys[lidx]])
            lidx += 1
            lidx %= (len(lkeys))

        total_cost = 0
        for c in word:
            total_cost += cost[ord(c) - ord('a')]
        return total_cost


# leetcode submit region end(Prohibit modification and deletion)


class MinimumNumberOfPushesToTypeWordIi(Solution):
    pass
