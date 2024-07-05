from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isNumber(self, s: str) -> bool:
        N = len(s)
        s = s.lower()
        if s[0] == 'e':
            return False
        if s == '.':
            return False

        if s and s[0] == '+' or s[0] == '-':
            s = s[1::]
        if s and s.count('.') > 1:
            return False
        if s and s.count('e') > 1:
            return False
        if s and s.find('.e') == 0:
            return False
        if s and s.find('e.') >= 0:
            return False


        s = s.replace(".", "0.0")
        s = s.replace("e+", "e")
        s = s.replace("e-", "e")

        checks = s.split('e')

        decimal_checks = []
        for i in range(len(checks)):
            if len(checks[i]) == 0:
                return False


        for i in range(len(checks)):
            cstr = checks[i]
            decimal_parts = cstr.split('.')
            if len(decimal_parts) > 2:
                return False
            if len(decimal_parts) > 1 and i > 0:
                return False
            for j in range(len(decimal_parts)):
                dpart = decimal_parts[j]
                if len(dpart) == 0:
                    continue
                decimal_checks.append(dpart)

        def validate(i, snum):
            if i == len(snum):
                return True
            if not snum[i].isnumeric():
                return False
            return validate(i+1, snum)

        while decimal_checks:
            if not validate(0, decimal_checks.pop()):
                return False
        return True



# leetcode submit region end(Prohibit modification and deletion)


class ValidNumber(Solution):
    pass
    