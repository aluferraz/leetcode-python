import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set(deadends)
        if "0000" in seen:
            return -1
        queue = collections.deque()
        queue.append([0, 0, 0, 0])
        steps = 0
        while len(queue) > 0:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                cur_str = "".join(str(c) for c in cur)
                if cur_str == target:
                    return steps
                seen.add(cur_str)
                for i in range(len(cur)):
                    new_arr = list(cur)
                    new_arr[i] = (cur[i] + 1) % 10
                    new_arr_str = "".join(str(c) for c in new_arr)
                    if new_arr_str not in seen:
                        seen.add(new_arr_str)
                        queue.append(new_arr)
                    new_arr = list(cur)
                    new_arr[i] = (cur[i] - 1)
                    if new_arr[i] < 0:
                        new_arr[i] = 9
                    new_arr_str = "".join(str(c) for c in new_arr)
                    if new_arr_str not in seen:
                        seen.add(new_arr_str)
                        queue.append(new_arr)
            steps += 1
        return -1


# leetcode submit region end(Prohibit modification and deletion)


class OpenTheLock(Solution):
    pass
