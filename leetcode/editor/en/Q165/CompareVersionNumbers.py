# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]
        while len(v1) < len(v2):
            v1.append(0)
        while len(v2) < len(v1):
            v2.append(0)

        N = len(v1)

        for i in range(N):
            if v1[i] > v2[i]:
                return 1
            if v2[i] > v1[i]:
                return -1
        return 0


# leetcode submit region end(Prohibit modification and deletion)


class CompareVersionNumbers(Solution):
    pass
