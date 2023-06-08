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
        cache = {}
        MOD = (10 ** 9) + 7

        def count(playlistLen, uniqueSongsPlayed):
            if playlistLen == goal:
                return 1 if uniqueSongsPlayed == N else 0
            if (playlistLen, uniqueSongsPlayed) in cache:
                return cache[(playlistLen, uniqueSongsPlayed)]
            repeatSong = (count(playlistLen + 1, uniqueSongsPlayed) * max(0, uniqueSongsPlayed - k)) % MOD
            newSong = ((N - uniqueSongsPlayed) * count(playlistLen + 1, uniqueSongsPlayed + 1)) % MOD

            cache[(playlistLen, uniqueSongsPlayed)] = repeatSong + newSong

            return cache[(playlistLen, uniqueSongsPlayed)]

        return count(0, 0)

        # leetcode submit region end(Prohibit modification and deletion)


class NumberOfMusicPlaylists(Solution):
    pass
