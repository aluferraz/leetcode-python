from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool] =
        """
        M = len(l)
        N = len(nums)
        ans = []
        for i in range(M):
            u,v = l[i],r[i]
            check = sorted(nums[u:v+1])
            if len(check) < 2:
                ans.append(False)
                continue
            d = check[1] - check[0]
            good = True
            for i in range(1, len(check)):
                if check[i] != check[i-1] + d:
                    good = False
                    break
            ans.append(good)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class ArithmeticSubarrays(Solution):
    pass
    