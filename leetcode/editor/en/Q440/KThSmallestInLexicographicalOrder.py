# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def countSteps(curr, n):
            steps = 0
            first = curr
            last = curr
            while first <= n:
                steps += min(last, n) - first + 1
                first *= 10
                last = last * 10 + 9
            return steps

        current = 1
        k -= 1  # Because we're looking for the k-th number (1-based index)

        while k > 0:
            steps = countSteps(current, n)
            if steps <= k:
                current += 1
                k -= steps
            else:
                current *= 10
                k -= 1

        return current


# leetcode submit region end(Prohibit modification and deletion)


class KThSmallestInLexicographicalOrder(Solution):
    pass
