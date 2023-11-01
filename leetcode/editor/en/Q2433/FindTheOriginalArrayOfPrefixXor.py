from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        N = len(pref)
        ans = [0] * N
        ans[0] = pref[0]

        for i in range(1, N):
            ans[i] = pref[i - 1] ^ pref[i]
        return ans
# leetcode submit region end(Prohibit modification and deletion)


class FindTheOriginalArrayOfPrefixXor(Solution):
    pass
    