# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        N = len(bombs)

        def explode(start):
            queue = collections.deque()
            queue.append(start)
            bombed = set()
            bombed.add(start)

            while len(queue) > 0:
                size = len(queue)
                for _ in range(size):
                    i = queue.popleft()
                    x_center, y_center, radius = bombs[i]
                    for j in range(0, N):
                        if j in bombed:
                            continue
                        x, y, _ = bombs[j]
                        insideRadius = ((x - x_center) ** 2) + ((y - y_center) ** 2) <= radius ** 2
                        if insideRadius:
                            queue.append(j)
                            bombed.add(j)
            return len(bombed)

        ans = 0
        for i in range(0, N):
            ans = max(ans, explode(i))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class DetonateTheMaximumBombs(Solution):
    pass
