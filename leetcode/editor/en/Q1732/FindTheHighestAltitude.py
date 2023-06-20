from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        ans = 0
        alt = 0
        for g in gain:
            alt += g
            ans = max(ans, alt)
        return ans

        
# leetcode submit region end(Prohibit modification and deletion)


class FindTheHighestAltitude(Solution):
    pass
    