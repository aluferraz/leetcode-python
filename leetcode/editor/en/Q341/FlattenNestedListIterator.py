import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        list = []

        def flatten(ni):
            if ni.isInteger():
                return list.append(ni.getInteger())
            arr = ni.getList()
            N = len(arr)
            if N == 0:
                return
            for i in range(N):
                if arr[i].isInteger():
                    list.append(arr[i].getInteger())
                else:
                    flatten(arr[i])
        for el in nestedList:
            flatten(el)
        self.list = collections.deque(list)

    def next(self):
        """
        :rtype: int
        """
        return self.list.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.list) > 0


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# leetcode submit region end(Prohibit modification and deletion)


class FlattenNestedListIterator(NestedIterator):
    pass
