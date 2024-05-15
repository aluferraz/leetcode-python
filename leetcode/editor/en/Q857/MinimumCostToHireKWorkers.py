import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        N = len(quality)
        costs = list(zip(wage, quality))
        costs.sort(key=lambda x: (x[0], -x[1]))  # lower salary, higher quality

        workers_choosen = [(costs[0][0], costs[0][0], costs[0][1])]
        _, f_salary, f_quality = workers_choosen[0]
        for i in range(1, N):
            c_salary, c_quality = costs[i]
            proportion = c_quality / f_quality
            if proportion * f_salary > c_salary:
                diff = (proportion * f_salary) - c_salary
                heapq.heappush(workers_choosen, (diff + c_salary, c_salary, c_quality))
            else:
                proportion = f_quality / c_quality

                diff = (proportion * c_salary) - f_salary
                heapq.heappush(workers_choosen, (diff + c_salary, c_salary, c_quality))

        ans = 0
        ans_workers = []
        for _ in range(k):
            _, s, q = heapq.heappop(workers_choosen)
            ans_workers.append((q, s))
        ans_workers.sort(key=lambda x: (x[0], -x[1]))
        ans = 0
        f_quality, f_salary = ans_workers[0]
        for i in range(k):
            c_quality, c_salary = ans_workers[i]
            proportion = (c_quality / f_quality)
            real_cost = max(c_salary, proportion * f_salary)
            ans += real_cost
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class MinimumCostToHireKWorkers(Solution):
    pass
