import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class FrequencyTracker(object):

    def __init__(self):
        self.arr = [0] * (10 ** 5 + 1)
        self.freqs = collections.defaultdict(int)

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        if self.freqs[self.arr[number]] != 0:
            self.freqs[self.arr[number]]  -= 1
        self.arr[number] += 1
        self.freqs[self.arr[number]] += 1

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        if self.arr[number] == 0:
            return
        self.freqs[self.arr[number]]  -= 1
        self.arr[number] = self.arr[number] - 1
        if self.arr[number] == 0:
            return
        self.freqs[self.arr[number]] += 1


    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        return self.freqs[frequency] > 0

    # Your FrequencyTracker object will be instantiated and called as such:


# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
# leetcode submit region end(Prohibit modification and deletion)


class FrequencyTracker(Solution):
    pass
