# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        if (d > len(jobDifficulty)):
            return -1

        hasCache = [[False for _ in range(0, len(jobDifficulty))] for i in range(0, d + 1)]
        cache = [[False for _ in range(0, len(jobDifficulty))] for i in range(0, d + 1)]

        def solve(i, d):
            if i >= len(jobDifficulty):
                return 0
            if d == 0:
                return 0
            if hasCache[d][i]:
                return cache[d][i]

            boundary = len(jobDifficulty) - d + 1
            jobCost = -1
            best = 100000000000

            for j in range(i, boundary):
                jobCost = max(jobCost, jobDifficulty[j])
                if d == 1:
                    best = jobCost
                else:
                    ansHere = jobCost + solve(j + 1, d - 1)
                    best = min(best, ansHere)

            cache[d][i] = best
            hasCache[d][i] = True
            return best

        return solve(0, d)

# leetcode submit region end(Prohibit modification and deletion)
