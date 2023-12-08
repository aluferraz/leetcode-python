from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        for i in range(len(num) -1,-1,-1):
            if int(num[i]) % 2 == 1:
                return num[0:i+1]
        return ""
        
# leetcode submit region end(Prohibit modification and deletion)


class LargestOddNumberInString(Solution):
    pass
    