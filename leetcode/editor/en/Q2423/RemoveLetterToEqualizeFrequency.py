from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        counter = [0 for _ in range(26)]
        maximum = -1
        maximumIdx = -1
        for i in range(len(word)):
            idx = ord(word[i]) - ord('a')
            counter[idx] += 1
            if counter[idx] > maximum:
                maximumIdx = idx
                maximum = counter[idx]

        counter[maximumIdx] -= 1
        freqs = set(counter)
        freqs.discard(0)
        if len(freqs) == 1:
            return True
        counter[maximumIdx] += 1
        freqs = set(counter)
        freqs.discard(0)
        if 1 in freqs and len(freqs) == 2:
            seen = False
            for c in counter:
                if c == 1:
                    if seen:
                        return False
                    seen = True
            return True
        return False


# leetcode submit region end(Prohibit modification and deletion)


class RemoveLetterToEqualizeFrequency(Solution):
    pass
