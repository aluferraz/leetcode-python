from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def haveConflict(self, event1, event2):
        """
        :type event1: List[str]
        :type event2: List[str]
        :rtype: bool
        """
        a = event1[1].split(':')
        b = event2[0].split(':')

        if int(a[0][0]) > 0 and int(b[0][0]) == 0:
            return False
        if int(a[0][0]) > int(b[0][0]):
            return True
        if int(a[0][0]) == int(b[0][0]):
            return int(a[0][0]) >= int(b[0][0])


# leetcode submit region end(Prohibit modification and deletion)


class DetermineIfTwoEventsHaveConflict(Solution):
    pass
