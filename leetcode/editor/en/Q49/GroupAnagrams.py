import collections
from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)
        return ans.values()

        
# leetcode submit region end(Prohibit modification and deletion)


class GroupAnagrams(Solution):
    pass