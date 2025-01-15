from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        cnt1 = [0] * 50
        cnt2 = [0] * 50
        ans = []
        for i in range(min(len(A), len(B))):
            cnt1[A[i]] += 1
            cnt2[B[i]] += 1
            ans_here = 0
            for j in range(50):
                if cnt1[j] == cnt2[j] and cnt1[j] > 0:
                    ans_here += 1
            ans.append(ans_here)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class FindThePrefixCommonArrayOfTwoArrays(Solution):
    pass
