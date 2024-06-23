import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exclusiveTime(self, N: int, logs: List[str]) -> List[int]:
        states = collections.defaultdict(list)

        for log in logs:
            eid, evt, timestamp = log.split(":")


# leetcode submit region end(Prohibit modification and deletion)


class ExclusiveTimeOfFunctions(Solution):
    pass
