import collections
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj_list = collections.defaultdict(list)
        for u, v in edges:
            adj_list[u - 1].append(v - 1)
            adj_list[v - 1].append(u - 1)

        distances1 = [(10 ** 20)] * n
        distances2 = [(10 ** 20)] * n
        min_heap = [(0, 0, 0, change)]
        distances1[0] = 0

        def dijkstra():

            while min_heap:
                current_dist, current_node, index, remaining_to_green = heapq.heappop(min_heap)
                if index == 0 and current_dist > distances1[current_node]:
                    continue
                if index == 1 and current_dist > distances2[current_node]:
                    continue
                if index == 1 and current_node == n - 1:
                    return current_dist

                if remaining_to_green <= 0:
                    current_dist += max((change + remaining_to_green), 0)
                    remaining_to_green = change
                remaining_to_green -= time

                for neighbor in adj_list[current_node]:
                    distance = current_dist + time

                    if distance < distances1[neighbor]:
                        distances2[neighbor] = distances1[neighbor]
                        distances1[neighbor] = distance
                        heapq.heappush(min_heap, (distance, neighbor, 0, remaining_to_green))
                    elif distance < distances2[neighbor]:
                        distances2[neighbor] = distance
                        heapq.heappush(min_heap, (distance, neighbor, 1, remaining_to_green))

            return -1

        return dijkstra()


# leetcode submit region end(Prohibit modification and deletion)


class SecondMinimumTimeToReachDestination(Solution):
    pass
