# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        N = len(ring)
        M = len(key)
        INF = 10 ** 20
        has_cache = [[False for _ in range(M)] for _ in range(N)]
        cache = [[INF for _ in range(M)] for _ in range(N)]

        def go(i, j):
            if j == M:
                return 0
            if has_cache[i][j]:
                return cache[i][j]
            has_cache[i][j] = True
            ans = INF
            for k in range(N):
                if ring[(i + k) % N] == key[j] or ring[(i - k) % N] == key[j]:
                    next_pos = (i + k) % N if ring[(i + k) % N] == key[j] else (i - k) % N
                    dist = min(k, N - k) + 1  # Min distance forward or backward, add one for pressing the center button
                    sub_ans = go(next_pos, j + 1)
                    ans = min(ans, dist + sub_ans)
            cache[i][j] = ans
            return ans

        return go(0, 0)
        # N = len(ring)
        # M = len(key)
        # INF = 10 ** 20
        # cache = [INF for _ in range(M)]
        # queue_cache = [[INF for _ in range(M)] for _ in range(N)]
        # queue = collections.deque()
        # queue.append((0, 0, 0))
        #
        # def enqueue(a, b, cost, q):
        #     if cost < cache[b] and cost < queue_cache[a][b]:
        #         q.append((a, b, cost))
        #         queue_cache[a][b] = cost
        #
        # while len(queue) > 0:
        #     size = len(queue)
        #     for _ in range(size):
        #         i, j, cost = queue.popleft()
        #         if ring[i] == ring[j]:
        #             cache[j] = min(cache[j], cost + 1)  # press it
        #             if j < M - 1:
        #                 enqueue((i + 1) % N, j + 1, cost + 2, queue)
        #                 enqueue((i - 1 if i > 0 else N - 1), j + 1, cost + 2, queue)
        #                 enqueue(i, j + 1, cost + 1, queue)
        #         else:
        #             enqueue((i + 1) % N, j, cost + 1, queue)
        #             enqueue((i - 1 if i > 0 else N - 1), j, cost + 1, queue)
        # return cache[M - 1]


# leetcode submit region end(Prohibit modification and deletion)


class FreedomTrail(Solution):
    pass
