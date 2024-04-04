from typing import List, Optional

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N = len(board)
        M = len(board[0])
        DIRECTIONS = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        def solve(i,j, k, visited):
            if not (i >= 0 and i < N and j >= 0 and j < M) or board[i][j] != word[k]:
                return False
            if k + 1 == len(word):
                return True

            visited.add((i,j))
            for di,dj in DIRECTIONS:
                if ((i+di), (j+dj)) in visited:
                    continue
                if solve((i+di), (j+dj), k+1, visited):
                    return True
            visited.remove((i,j))
            return False

        for i in range(N):
            for j in range(M):
                if board[i][j] == word[0]:
                    if solve(i,j,0,set()):
                        return True
        return False

# leetcode submit region end(Prohibit modification and deletion)


class WordSearch(Solution):
    pass