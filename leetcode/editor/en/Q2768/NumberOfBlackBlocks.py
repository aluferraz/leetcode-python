import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countBlackBlocks(self, m, n, coordinates):
        """
        :type m: int
        :type n: int
        :type coordinates: List[List[int]]
        :rtype: List[int]
        """

        ans = [0 for _ in range(5)]

        coord_map = collections.defaultdict(int)
        block_sum = collections.defaultdict(int)

        for row, col in coordinates:
            coord_map[(row, col)] += 1

        def is_valid_idx(row, col):
            return row >= 0 and row < m and col >= 0 and col < n

        for row, col in coordinates:
            if is_valid_idx(row + 1, col + 1):  # Top left block
                block_sum[(row + 1, col + 1)] += 1
            if is_valid_idx(row - 1, col - 1):  # Bottom right block
                block_sum[(row, col)] += 1
            if is_valid_idx(row, col + 1) and is_valid_idx(row - 1, col + 1):  # Bottom left block
                block_sum[(row, col + 1)] += 1
            if is_valid_idx(row + 1, col) and is_valid_idx(row, col - 1):  # top right block
                block_sum[(row + 1, col)] += 1

        total_blocks = (m - 1) * (n - 1)

        for block_id in block_sum:
            black_cells = block_sum[block_id]
            ans[black_cells] += 1
        ans[0] = total_blocks - len(block_sum)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfBlackBlocks(Solution):
    pass
