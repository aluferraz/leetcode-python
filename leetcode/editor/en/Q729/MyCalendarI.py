# leetcode submit region begin(Prohibit modification and deletion)
import sortedcontainers


class MyCalendar:

    def __init__(self):
        self.starts = sortedcontainers.SortedDict()

    def bin_search_before(self, time):
        left = 0
        right = len(self.starts)
        keys = list(self.starts.keys())
        ans = -1
        while left < right:
            mid = (left + right) // 2
            if keys[mid] <= time:
                ans = mid
                left = mid + 1
            else:
                right = mid
        return ans

    def book(self, start: int, end: int) -> bool:
        latest_start_idx = self.bin_search_before(start)
        start_keys = list(self.starts.keys())
        if latest_start_idx >= 0:
            latest_start = start_keys[latest_start_idx]
            end_time = self.starts[latest_start]
            if end_time > start:
                return False
        if latest_start_idx + 1 < len(start_keys) \
                and end > start_keys[latest_start_idx + 1]:
            return False

        self.starts[start] = end
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# leetcode submit region end(Prohibit modification and deletion)


class MyCalendarI(MyCalendar):
    pass
