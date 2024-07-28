import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj_list = {}
        INF = 10 ** 20
        for i in range(26):
            adj_list[i] = [INF] * 26
        for i in range(len(original)):
            source_idx = ord(original[i]) - ord('a')
            dest_idx = ord(changed[i]) - ord('a')
            adj_list[source_idx][dest_idx] = min(adj_list[source_idx][dest_idx], cost[i])

        def dijkstra(start):
            min_heap = [(0, start)]
            distances = [(10 ** 20)] * 26
            distances[start] = 0

            while min_heap:
                current_dist, current_node = heapq.heappop(min_heap)

                if current_dist > distances[current_node]:
                    continue
                for neighbor in range(26):
                    if neighbor == start:
                        continue
                    weight = adj_list[current_node][neighbor]
                    distance = current_dist + weight

                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(min_heap, (distance, neighbor))

            adj_list[start] = distances
            return distances

        for letter_idx in adj_list.keys():
            dijkstra(letter_idx)

        total_cost = 0
        N = len(source)
        for i in range(N):
            source_str_idx = ord(source[i]) - ord('a')
            target_idx = ord(target[i]) - ord('a')
            total_cost += adj_list[source_str_idx][target_idx]
        if total_cost >= INF:
            return -1
        return total_cost


# leetcode submit region end(Prohibit modification and deletion)


class MinimumCostToConvertStringI(Solution):
    pass
