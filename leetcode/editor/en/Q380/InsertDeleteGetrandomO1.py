import random
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class RandomizedSet:

    def __init__(self):
        self.numbers = {}
        self.numbers_arr = []


    def insert(self, val: int) -> bool:
        if val in self.numbers:
            return False
        self.numbers[val] = len(self.numbers)
        self.numbers_arr.append(val)
        return True


    def remove(self, val: int) -> bool:
        if val in self.numbers:

            num_indx = self.numbers[val]
            last_number = self.numbers_arr[-1]
            self.numbers_arr[num_indx] = self.numbers_arr[-1]
            self.numbers_arr[-1] = val
            self.numbers.pop(val)
            self.numbers_arr.pop()
            if last_number != val:
                self.numbers[last_number] = num_indx
            return True
        return False
        

    def getRandom(self) -> int:
        return self.numbers_arr[random.randint(0,len(self.numbers_arr) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# leetcode submit region end(Prohibit modification and deletion)


class InsertDeleteGetrandomO1(RandomizedSet):
    pass