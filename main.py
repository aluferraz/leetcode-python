from contest import Solution
from leetcode.editor.en.Q1255.MaximumScoreWordsFormedByLetters import MaximumScoreWordsFormedByLetters

dummy = Solution()

if __name__ == '__main__':
    print(MaximumScoreWordsFormedByLetters().maxScoreWords(["dog", "cat", "dad", "good"],
                                                           ["a", "a", "c", "d", "d", "d", "g", "o", "o"],
                                                           [
                                                               1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0,
                                                               0, 0, 0, 0, 0, 0, 0]))
