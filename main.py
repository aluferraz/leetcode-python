from contest import Solution
from leetcode.editor.en.Q1463.CherryPickupIi import CherryPickupIi

dummy = Solution()

if __name__ == '__main__':
#  print(CherryPickupIi().cherryPickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))

    S = "one+two-one-one+two+one"
    ans = 0

    S = S.replace("one", "1")
    S = S.replace("two", "2")
    N = len(S)


    def evaluate(i, flip):
        if i == N:
            return 0
        num = 0
        if S[i] == "-":
            return evaluate(i + 1, True)
        elif S[i] == "+":
            return evaluate(i + 1, False)
        else:
            num = int(S[i])
            if flip:
                num *= -1
        return num + evaluate(i + 1,False)

    print(evaluate(0,False))



