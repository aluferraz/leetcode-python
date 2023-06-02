import collections


# leetcode submit region begin(Prohibit modification and deletion)
class UndergroundSystem(object):

    def __init__(self):
        self.times = collections.defaultdict(lambda: [0, 0])
        self.inProgress = collections.defaultdict(int)

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """

        self.inProgress[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        info = self.inProgress[id]
        fromStation = info[0]
        toStation = stationName
        startTime = info[1]
        travelTime = t - startTime
        self.inProgress.pop(id)
        travelKey = (fromStation, toStation)
        timeInfo = self.times[travelKey]
        timeInfo[0] += travelTime
        timeInfo[1] += 1

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        timeInfo = self.times[(startStation, endStation)]
        return timeInfo[0] / timeInfo[1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# leetcode submit region end(Prohibit modification and deletion)


class DesignUndergroundSystem(UndergroundSystem):
    pass
