# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        f = collections.defaultdict(int)
        total = 0
        is_odd = 0
        f[is_odd] += 1
        for c in word:
            d = ord(c) - ord('a')
            # Counting only even occurrences, so if the letter is even, must have seen an even occurrence
            # if letter is odd, must have seen odd occurences
            is_odd ^= (1 << d)
            total += f[is_odd]
            for i in range(10):
                # Now we try to make each possible letter as the odd one.
                # So, if the letter is odd now, we must have seen an even occurrence previously, so it stays odd
                # otherwise if the letter is even now,
                # for it to be the odd one I must have seen an odd occurrence previously.
                total += f[is_odd ^ (1 << i)]
            f[is_odd] += 1

        return total


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfWonderfulSubstrings(Solution):
    pass
