

import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
import sortedcontainers
class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        N = len(foods)
        self.cuisines = collections.defaultdict(set)
        self.foods_rating = collections.defaultdict(sortedcontainers.SortedList)
        self.foods_rating_map = {}
        for i in range(N):
            self.cuisines[foods[i]].add(cuisines[i])
            self.foods_rating[cuisines[i]].add((-ratings[i], foods[i]))
            self.foods_rating_map[(foods[i], cuisines[i])] = -ratings[i]

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        cuisines = self.cuisines[food]
        for cuisine in cuisines:
            rating_key = (food, cuisine)
            current_rating = self.foods_rating_map[rating_key]
            self.foods_rating_map.pop(rating_key)
            self.foods_rating[cuisine].remove((current_rating, food))
            self.foods_rating_map[rating_key] = -newRating
            self.foods_rating[cuisine].add((-newRating, food))

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        return self.foods_rating[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
# leetcode submit region end(Prohibit modification and deletion)


class DesignAFoodRatingSystem(FoodRatings):
    pass
