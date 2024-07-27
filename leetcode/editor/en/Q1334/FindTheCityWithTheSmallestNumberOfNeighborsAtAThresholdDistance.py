import collections
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Create adjacency list
        adj_list = collections.defaultdict(list)
        for source, dest, weight in edges:
            adj_list[source].append((dest, weight))
            adj_list[dest].append((source, weight))

        def dijkstra(start):
            min_heap = [(0, start)]
            distances = [(10 ** 20)] * n
            distances[start] = 0

            while min_heap:
                current_dist, current_node = heapq.heappop(min_heap)

                if current_dist > distances[current_node]:
                    continue

                for neighbor, weight in adj_list[current_node]:
                    distance = current_dist + weight

                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(min_heap, (distance, neighbor))

            # Count cities reachable within the distance threshold
            reachable_cities = sum(d <= distanceThreshold for d in distances) - 1
            return reachable_cities

        min_reachable = 10 ** 20
        answer = -1

        for i in range(n):
            reachable_count = dijkstra(i)
            if reachable_count <= min_reachable:
                min_reachable = reachable_count
                answer = i

        return answer


# leetcode submit region end(Prohibit modification and deletion)


class FindTheCityWithTheSmallestNumberOfNeighborsAtAThresholdDistance(Solution):
    pass
