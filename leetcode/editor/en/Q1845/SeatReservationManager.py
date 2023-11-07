import sortedcontainers

import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.free_seats = [i for i in range(1, n + 1)]
        self.reserved_seats = set()

    def reserve(self):
        """
        :rtype: int
        """
        seat = heapq.heappop(self.free_seats)
        self.reserved_seats.add(seat)
        return seat

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        if not (seatNumber in self.reserved_seats):
            return
        self.reserved_seats.discard(seatNumber)
        heapq.heappush(self.free_seats, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
# leetcode submit region end(Prohibit modification and deletion)


class SeatReservationManager(Solution):
    pass
