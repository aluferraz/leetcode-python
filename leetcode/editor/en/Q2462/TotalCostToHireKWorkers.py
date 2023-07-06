import collections
import heapq
import math
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        workersCosts = [(w, i) for (i, w) in enumerate(costs)]
        first = collections.deque()
        last = collections.deque()

        N = len(costs)
        INF = 10 ** 20
        for i in range(0, N // 2):
            first.append(workersCosts[i])
        for i in range(N // 2, N):
            last.append(workersCosts[i])

        candidatesHeap = []

        cost = 0
        firstCandidatesMissing = candidates
        lastCandidatesMissing = candidates

        while k > 0:
            while len(first) > 0 and firstCandidatesMissing > 0:
                heapq.heappush(candidatesHeap, first.popleft())
                firstCandidatesMissing -= 1
            while len(last) > 0 and lastCandidatesMissing > 0:
                heapq.heappush(candidatesHeap, last.pop())
                lastCandidatesMissing -= 1
            while firstCandidatesMissing > 0 and len(last) > 0:
                (w, j) = last.popleft()
                j -= N // 2
                heapq.heappush(candidatesHeap, (w, j))
                firstCandidatesMissing -= 1
            while lastCandidatesMissing > 0 and len(first) > 0:
                (w, j) = first.pop()
                j += N // 2
                heapq.heappush(candidatesHeap, (w, j))
                lastCandidatesMissing -= 1

            (nextWorkerCost, i) = heapq.heappop(candidatesHeap)
            cost += nextWorkerCost
            if i < N // 2:
                firstCandidatesMissing += 1
            else:
                lastCandidatesMissing += 1
            k -= 1
        return cost


# leetcode submit region end(Prohibit modification and deletion)


class TotalCostToHireKWorkers(Solution):
    pass
