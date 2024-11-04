from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        N = len(folder)
        ans = [folder[0]]
        for i in range(1, N):
            path = "".join([ans[-1], "/"])
            if not folder[i].startswith(path):
                ans.append(folder[i])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class RemoveSubFoldersFromTheFilesystem(Solution):
    pass
