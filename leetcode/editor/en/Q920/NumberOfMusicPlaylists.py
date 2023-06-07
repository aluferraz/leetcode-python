# leetcode submit region begin(Prohibit modification and deletion)
import collections
import math


class Solution(object):
    def numMusicPlaylists(self, N, goal, k):
        """
        :type n: int
        :type goal: int
        :type k: int
        :rtype: int
        """

        # playlist = [0 for _ in range(goal)]
        #
        # def count(songs, i, nextRepeat):
        #     if i >= goal:
        #         return
        #     if i == nextRepeat and i - k - 1 >= 0:
        #         songs = N
        #     nextRepeat = i + k + 1
        #     playlist[i] = songs
        #     count(songs - 1, i + 1, nextRepeat)
        #
        # count(N, 0, 0)
        #
        # ans = 1
        # for p in playlist:
        #     ans *= p
        # return ans


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfMusicPlaylists(Solution):
    pass
