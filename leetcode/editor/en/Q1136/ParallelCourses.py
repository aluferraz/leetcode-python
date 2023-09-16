import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumSemesters(self, N, relations):
        """
        :type n: int
        :type relations: List[List[int]]
        :rtype: int
        """
        in_degree = [0] * (N + 1)

        adj_list = collections.defaultdict(list)

        for pre_req, next_course in relations:
            in_degree[next_course] += 1
            adj_list[next_course].append(pre_req)
            adj_list[pre_req].append(next_course)

        done = 0
        taken = [False] * (N + 1)
        ans = 0
        while done < N:
            ans += 1
            can_do = False
            reduce_degree = []
            for i in range(1, N + 1):
                if in_degree[i] == 0 and not taken[i]:
                    done += 1
                    can_do = True
                    taken[i] = True
                    for next_course in adj_list[i]:
                        reduce_degree.append(next_course)
            while len(reduce_degree) > 0:
                in_degree[reduce_degree.pop()] -= 1
            if not can_do:
                return -1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class ParallelCourses(Solution):
    pass
