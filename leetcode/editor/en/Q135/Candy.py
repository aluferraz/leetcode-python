from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        N = len(ratings)
        INF = 10 ** 20
        candies = [1] * N

        def build_candies():
            for i in range(N):
                prev_child_rating = INF
                prev_candy = 0
                if i > 0:
                    prev_child_rating = ratings[i - 1]
                    prev_candy = candies[i - 1]
                if ratings[i] > prev_child_rating:
                    candies[i] = prev_candy + 1

        def build_candies_rev():
            for i in range(N - 2, -1, -1):
                next_child_rating = ratings[i + 1]
                next_candy = candies[i + 1]
                if ratings[i] > next_child_rating:
                    candies[i] = max(candies[i], next_candy + 1)

        build_candies()
        build_candies_rev()

        # print(candies)
        return sum(candies)


# leetcode submit region end(Prohibit modification and deletion)


class Candy(Solution):
    pass
