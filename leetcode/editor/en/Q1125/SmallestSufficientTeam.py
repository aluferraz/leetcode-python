from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        req_skills_mask = 0
        skills_map = {}
        N = len(req_skills)
        M = len(people)
        INF = 10 ** 20
        target = (1 << N) - 1
        for i in range(N):
            req_skills_mask |= (1 << i)
            skills_map[req_skills[i]] = i
        people_mask = [0 for _ in range(M)]
        for i in range(M):
            mask = 0
            for skill in people[i]:
                skill_mask = skills_map[skill]
                mask |= (1 << skill_mask)
            people_mask[i] = mask

        cache = {}

        def best(i, mask):
            if mask == target:
                return (0, 0)
            if i == M:
                return (INF, 0)
            if (i, mask) in cache:
                return cache[(i, mask)]
            useSize, useTeam = best(i + 1, mask | people_mask[i])
            useSize += 1
            skipSize, skipTeam = best(i + 1, mask)
            if useSize < skipSize:
                ans = (useSize, useTeam | (1 << i))
            else:
                ans = (skipSize, skipTeam)
            cache[(i, mask)] = ans
            return ans

        size, team = best(0, 0)
        best = []
        teamStr = bin(team)[2:]
        pos = 0
        for i in range(len(teamStr) - 1, -1, -1):
            if teamStr[i] == '1':
                best.append(pos)
            pos += 1

        return best

    # leetcode submit region end(Prohibit modification and deletion)


class SmallestSufficientTeam(Solution):
    pass
