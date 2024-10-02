import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mod_arr = [x % k for x in arr]
        seen = collections.defaultdict(list)
        N = len(arr)
        has_pair = [False] * N
        for i in range(N):
            diff = k - mod_arr[i]
            if diff in seen:
                has_pair[i] = True
                has_pair[seen[diff].pop()] = True
                if len(seen[diff]) == 0:
                    seen.pop(diff)
            else:
                if diff == k:
                    seen[k].append(i)
                else:
                    seen[mod_arr[i]].append(i)
        all_paired = True
        for p in has_pair:
            all_paired = all_paired and p
        return all_paired


# leetcode submit region end(Prohibit modification and deletion)


class CheckIfArrayPairsAreDivisibleByK(Solution):
    pass
