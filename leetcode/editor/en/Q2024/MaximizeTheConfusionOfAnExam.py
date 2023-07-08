from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        N = len(answerKey)
        answers = [0 if ans == 'F' else 1 for ans in answerKey]

        def getPresum(arr):
            pre = [0 for _ in range(len(arr))]
            pre[0] = arr[0]
            for i in range(1, len(arr)):
                pre[i] = pre[i - 1] + arr[i]
            return pre

        def good(value, begin, end):
            if value == 0 or \
                    value == (end - begin + 1) or \
                    value + k >= (end - begin + 1) or \
                    value - k <= 0:
                return True
            return False

        presum = getPresum(answers)

        def guessBest(i):
            left = i
            right = N
            start = 0
            if i > 0:
                start = presum[i - 1]
            best = 0
            while left < right:
                mid = (left + right) // 2
                rangeValue = presum[mid] - start
                if good(rangeValue, i, mid):
                    best = (mid - i + 1)
                    left = mid + 1
                else:
                    right = mid
            return best

        ans = 0
        for i in range(N):
            ans = max(ans, guessBest(i))

        return ans

        # leetcode submit region end(Prohibit modification and deletion)


class MaximizeTheConfusionOfAnExam(Solution):
    pass
