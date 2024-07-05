from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        ans = 0
        for _ in range(2):
            max_until_forward = [0] * N
            min_until_forward = [0] * N

            for i in range(1, N):
                if height[i] > height[max_until_forward[i - 1]]:
                    max_until_forward[i] = i
                else:
                    max_until_forward[i] = max_until_forward[i - 1]
                if height[i] < height[min_until_forward[i - 1]]:
                    min_until_forward[i] = i
                else:
                    min_until_forward[i] = min_until_forward[i - 1]

            for i in range(1, N):
                option_1 = min(height[i], height[max_until_forward[i - 1]]) * (i - max_until_forward[i - 1])
                option_2 = min(height[i], height[min_until_forward[i - 1]]) * (i - min_until_forward[i - 1])
                best_option = max(option_1, option_2)
                ans = max(best_option, ans)
            height.reverse()

        return ans
# leetcode submit region end(Prohibit modification and deletion)


class ContainerWithMostWater(Solution):
    pass
    