# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numMusicPlaylists(self, N, goal, k):
        """
        :type n: int
        :type goal: int
        :type k: int
        :rtype: int
        """
        # playlist = []
        # songs = [i for i in range(1, N + 1)]
        # canBeUsed = [0 for i in range(0, N + 1)]
        #
        # cache = {}
        #
        # def count(i):
        #     if len(playlist) == goal:
        #         return 1
        #     ans = 0
        #     for j in range(0, N):
        #         nextSong = songs[((i % N) + j) % N]
        #         if i < canBeUsed[nextSong]:
        #             continue
        #         canBeUsed[nextSong] = i + 1 + k
        #         playlist.append(nextSong)
        #         ans += count((i + 1))
        #         playlist.pop()
        #
        #     return ans
        #
        # return count(0)


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfMusicPlaylists(Solution):
    pass
