import collections
import heapq
import sortedcontainers
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        accounts = collections.defaultdict(int)
        for (f, t, v) in transactions:
            accounts[f] -= v
            accounts[t] += v

        creditsAcc = []  # sortedcontainers.SortedList(key=lambda x: x[0])
        debitsAcc = collections.deque()  # sortedcontainers.SortedList(key=lambda x: x[0])

        for (acc, bal) in accounts.items():
            if bal > 0:
                creditsAcc.append(bal)
            elif bal < 0:
                debitsAcc.append(bal)

        N = len(creditsAcc)
        M = len(debitsAcc)
        if M == 0:
            return 0

        def count(i):
            if i == M:
                return 0

            ans = 10 ** 20
            debt = debitsAcc[i]
            if debt == 0:
                return count(i + 1)
            # start = take_closest(creditsAcc, debt)

            for j in range(N):
                if creditsAcc[j] > 0:
                    cred = creditsAcc[j]
                    transaction = min(abs(debt), abs(cred))
                    debtBalance = -abs(debt) + transaction
                    credBalance = cred - transaction

                    debitsAcc[i] = debtBalance
                    creditsAcc[j] = credBalance

                    ans = min(ans, 1 + count(i))

                    creditsAcc[j] = cred
                    debitsAcc[i] = debt

            return ans

        ans = 10 ** 20
        for i in range(M):
            ans = min(ans, count(0))
            debitsAcc.append(debitsAcc.popleft())
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class OptimalAccountBalancing(Solution):
    pass
