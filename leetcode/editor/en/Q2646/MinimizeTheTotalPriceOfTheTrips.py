import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumTotalPrice(self, N, edges, price, trips):
        """
        :type n: int
        :type edges: List[List[int]]
        :type price: List[int]
        :type trips: List[List[int]]
        :rtype: int
        """
        adj_list = collections.defaultdict(set)
        INF = 10 ** 20
        for u, v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)

        counter = [0 for _ in range(N)]

        def bfs(from_node, to_node):
            queue = collections.deque()
            path = [-1 for _ in range(N)]
            best_cost = [INF for _ in range(N)]
            queue.append(from_node)
            best_cost[from_node] = 0
            found = False
            while len(queue) > 0:
                size = len(queue)
                for _ in range(size):
                    if found:
                        break
                    node = queue.popleft()
                    for next_node in adj_list[node]:
                        node_price = price[next_node]
                        if best_cost[node] + node_price < best_cost[next_node]:
                            queue.append(next_node)
                            path[next_node] = node
                            best_cost[next_node] = best_cost[node] + node_price
                        if next_node == to_node:
                            found = True
                if found:
                    break
            real_path = collections.deque()

            current = to_node
            while path[current] != -1:
                real_path.appendleft(current)
                current = path[current]
            if len(real_path) == 0 or real_path[0] != from_node:
                real_path.appendleft(from_node)
            return real_path

        for f, t in trips:
            path = bfs(f, t)
            for node in path:
                counter[node] += 1

        cache_best = {}

        def best_price(i, p, canHalf):
            if i == N:
                return 0
            if (i, p, canHalf) in cache_best:
                return cache_best[(i, p, canHalf)]
            ans = INF
            if canHalf:
                total_cost_half = (price[i] // 2) * counter[i]
                for next_node in adj_list[i]:
                    if next_node == p:
                        continue
                    total_cost_half += best_price(next_node, i, False)
                ans = min(ans, total_cost_half)
            total_cost_full = price[i] * counter[i]
            for next_node in adj_list[i]:
                if next_node == p:
                    continue
                total_cost_full += best_price(next_node, i, True)
            ans = min(ans, total_cost_full)
            cache_best[(i, p, canHalf)] = ans
            return ans

        minimum = INF
        for i in range(N):
            minimum = min(minimum, best_price(i, -1, True))
        return minimum

    # leetcode submit region end(Prohibit modification and deletion)


class MinimizeTheTotalPriceOfTheTrips(Solution):
    pass
