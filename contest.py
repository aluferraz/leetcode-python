import collections
import heapq
from typing import List


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        N = len(nums)
        MOD = (10 ** 9) + 7

        adj_list = collections.defaultdict(set)
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    adj_list[nums[i]].add(nums[j])
        visited = set()

        cache = {}
        comb = set()

        def count(i):
            visited.add(i)
            if len(visited) == N:
                visited.discard(i)
                comb.add(str(visited))
                return 1
            if (str(visited)) in cache:
                return cache[str(visited)]
            ans = 0
            for j in adj_list[i]:
                if j not in visited:
                    ans += (count(j) % MOD)
            visited.discard(i)
            cache[str(visited)] = ans
            return ans

        ans = 0
        for i in range(N):
            visited = set()
            comb = set()
            ans += count(nums[i]) % MOD
        return ans
