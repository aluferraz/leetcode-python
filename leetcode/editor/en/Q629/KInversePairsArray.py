# leetcode submit region begin(Prohibit modification and deletion)
import sortedcontainers


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:

        nums = [i for i in range(1, n + 1)]
        N = len(nums)

        def swap(arr, i, j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

        def go(i):
            if i == N:
                inversions = 0
                min_list = sortedcontainers.SortedList()
                for i in range(N):
                    greater_than = min_list.bisect_left(nums[i])
                    inversions += len(min_list) - greater_than
                    min_list.add(nums[i])
                if inversions == k:
                    return 1
                return 0
            ans = 0
            for j in range(i, N):
                swap(nums, i, j)
                ans += go(i + 1)
                swap(nums, i, j)
            return ans
        return go(0)

# leetcode submit region end(Prohibit modification and deletion)


class KInversePairsArray(Solution):
    pass
