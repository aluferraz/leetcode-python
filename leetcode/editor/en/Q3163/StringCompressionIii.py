# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def compressedString(self, word: str) -> str:
        arr = []
        ans = []
        counter = 0
        for c in word:
            if len(arr) == 0:
                arr.append(c)
                counter = 1
            elif arr[-1] == c and counter < 9:
                counter += 1
            else:
                ans.append(str(counter))
                ans.append(arr.pop())
                arr.append(c)
                counter = 1
        if len(arr) > 0:
            ans.append(str(counter))
            ans.append(arr.pop())
        return "".join(ans)


# leetcode submit region end(Prohibit modification and deletion)


class StringCompressionIii(Solution):
    pass
