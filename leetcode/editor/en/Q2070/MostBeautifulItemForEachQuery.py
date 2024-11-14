from typing import List

import sortedcontainers


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        best_item = sortedcontainers.SortedDict()
        for p, i in items:
            if p not in items:
                best_item[p] = i
            best_item[p] = max(best_item[p], i)
        N = len(queries)
        ans = [0] * N
        keys = list(best_item.keys())
        max_seen = -1
        for k in keys:
            max_seen = max(max_seen, best_item[k])
            best_item[k] = max_seen

        def find(limit):
            left = 0
            right = len(keys)
            ans = 0
            while left < right:
                mid = (left + right) // 2
                val = keys[mid]
                if val > limit:
                    right = mid
                else:
                    ans = mid
                    left = mid + 1
            return ans

        for i in range(N):
            q = queries[i]
            idx = find(q)
            if idx < len(keys) and keys[idx] <= q:
                ans[i] = best_item[keys[idx]]

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MostBeautifulItemForEachQuery(Solution):
    pass
