from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        # Create an adjacency matrix to track reachability
        reachable = [[False] * numCourses for _ in range(numCourses)]

        # Mark direct prerequisites
        for u, v in prerequisites:
            reachable[u][v] = True

        # Use Floyd-Warshall to compute transitive closure
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])

        # Answer the queries
        return [reachable[u][v] for u, v in queries]


# leetcode submit region end(Prohibit modification and deletion)


class CourseScheduleIv(Solution):
    pass
