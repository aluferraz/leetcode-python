from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        N = len(arr)
        prexor = [0] * N
        prexor[0] = arr[0]
        for i in range(1, N):
            prexor[i] = prexor[i - 1] ^ arr[i]
        ans = []
        for left, right in queries:
            if left > 0:
                ans.append(prexor[right] ^ prexor[left - 1])
            else:
                ans.append(prexor[right])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class XorQueriesOfASubarray(Solution):
    pass
