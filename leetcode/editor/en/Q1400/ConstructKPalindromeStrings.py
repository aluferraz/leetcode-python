# leetcode submit region begin(Prohibit modification and deletion)

from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # If k is greater than the length of the string, it's impossible
        if k > len(s):
            return False

        # Count the frequency of each character in the string
        char_counts = Counter(s)

        # Count how many characters have odd frequencies
        num_odd = sum(1 for count in char_counts.values() if count % 2 == 1)

        # The minimum number of palindromic substrings needed is the number of odd counts
        min_k = num_odd

        # The maximum number of palindromic substrings is the length of the string
        max_k = len(s)

        # Check if k is within the feasible range
        return min_k <= k <= max_k


# leetcode submit region end(Prohibit modification and deletion)


class ConstructKPalindromeStrings(Solution):
    pass
