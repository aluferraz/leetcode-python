import collections
from operator import iadd, isub


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return len(s2) >= len(s1) and (c1 := collections.Counter(s2[:len(s1)])) and (
            c2 := collections.Counter(s1)) and c1 == c2 or any(
            map(lambda i: iadd(c1, {s2[i]: 1}) and isub(c1, {s2[i - len(s1)]: 1}) and c1 == c2,
                range(len(s1), len(s2))))


# leetcode submit region end(Prohibit modification and deletion)


class PermutationInString(Solution):
    pass
