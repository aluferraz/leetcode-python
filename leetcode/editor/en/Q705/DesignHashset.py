
# leetcode submit region begin(Prohibit modification and deletion)
class MyHashSet(object):

    def __init__(self):
        self.hashset = [False for _ in range(0, (10**6) + 1) ]
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashset[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashset[key] = False

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self.hashset[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# leetcode submit region end(Prohibit modification and deletion)


class DesignHashset(Solution):
    pass
    