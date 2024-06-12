from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        rel_order = {}
        N = len(arr1)
        M = len(arr2)
        for i in range(M):
            rel_order[arr2[i]] = i
        relative_sort = []
        remaining = []
        for i in range(N):
            num = arr1[i]
            if num in rel_order:
                relative_sort.append((rel_order[num], num))
            else:
                remaining.append(num)
        relative_sort.sort()
        remaining.sort()
        ans = []
        for i in range(len(relative_sort)):
            ans.append(relative_sort[i][1])
        for n in remaining:
            ans.append(n)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class RelativeSortArray(Solution):
    pass
