from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """

        alice_moves = 0
        bob_moves = 0
        N = len(colors)
        for i in range(1, N - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == 'B':
                    bob_moves += 1
                else:
                    alice_moves += 1

        def can_win(player, alice_moves, bob_moves):
            if player == 0:
                if alice_moves == 0:
                    return False
                return can_win(1, alice_moves - 1, bob_moves)
            else:
                if bob_moves == 0:
                    return True
                return can_win(0, alice_moves, bob_moves - 1)

        return can_win(0, alice_moves, bob_moves)


# leetcode submit region end(Prohibit modification and deletion)


class RemoveColoredPiecesIfBothNeighborsAreTheSameColor(Solution):
    pass
