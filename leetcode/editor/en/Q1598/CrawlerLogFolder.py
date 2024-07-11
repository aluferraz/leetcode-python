from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folders = 0
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                folders = max(folders - 1, 0)
            else:
                folders += 1
        return folders


# leetcode submit region end(Prohibit modification and deletion)


class CrawlerLogFolder(Solution):
    pass
