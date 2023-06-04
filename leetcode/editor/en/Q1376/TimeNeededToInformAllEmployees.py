# leetcode submit region begin(Prohibit modification and deletion)
import collections
import heapq


class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        START = 1
        END = -1
        queue = collections.deque()

        queue.append([headID, 0])
        adj_list = collections.defaultdict(list)
        for i in range(n):
            if i == headID:
                continue
            adj_list[manager[i]].append(i)

        timeline = []
        while len(queue) > 0:
            size = len(queue)
            for _ in range(size):
                current, time = queue.popleft()
                subordinates = adj_list[current]
                if len(subordinates) == 0:
                    continue
                heapq.heappush(timeline, [time, START])
                time += informTime[current]
                heapq.heappush(timeline, [time, END])
                for nextEmployee in subordinates:
                    queue.append([nextEmployee, time])

        state = 0
        ans = 0
        while len(timeline) > 0:
            time, event = heapq.heappop(timeline)
            state += event
            if state == 0:
                ans = max(time, ans)

        return ans


# leetcode submit region end(Prohibit modification and deletion)


class TimeNeededToInformAllEmployees(Solution):
    pass
