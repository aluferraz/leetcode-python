# leetcode submit region begin(Prohibit modification and deletion)
from functools import cache


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split(' ')
        s2 = sentence2.split(' ')
        N = len(s1)
        M = len(s2)

        @cache
        def go(i, j, is_inserting, can_insert, insert_arr):
            if i >= N and j >= M:
                return True
            if i >= N and j < M:
                if is_inserting and insert_arr == 1:
                    return True
                return can_insert
            if i < N and j >= M:
                if is_inserting and insert_arr == 0:
                    return True
                return can_insert
            if s1[i] == s2[j]:
                if go(i + 1, j + 1, False, not is_inserting and can_insert, insert_arr):
                    return True
            if is_inserting:
                if insert_arr == 0:
                    return go(i + 1, j, is_inserting, not is_inserting, insert_arr)
                else:
                    return go(i, j + 1, is_inserting, not is_inserting, insert_arr)
            if can_insert:
                return go(i + 1, j, True, False, 0) or \
                    go(i, j + 1, True, False, 1)
            return False

        return go(0, 0, False, True, -1)


# leetcode submit region end(Prohibit modification and deletion)


class SentenceSimilarityIii(Solution):
    pass
