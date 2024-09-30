class MyCalendarTwo:
    def __init__(self):
        self.events = []
        self.double_booked = []

    def book(self, start: int, end: int) -> bool:
        for event in self.double_booked:
            if event[0] <= start < event[1] or event[0] < end < event[1] or (start <= event[0] and end >= event[1]):
                return False

        for event in self.events:
            if event[0] <= start < event[1] or event[0] < end < event[1] or (start <= event[0] and end >= event[1]):
                self.double_booked.append((max(start, event[0]), min(end, event[1])))

        self.events.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
# leetcode submit region end(Prohibit modification and deletion)


class MyCalendarIi(MyCalendarTwo):
    pass
