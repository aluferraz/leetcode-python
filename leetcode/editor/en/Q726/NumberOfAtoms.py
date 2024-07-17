import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        counter = collections.defaultdict(int)
        N = len(formula)
        idx = 0

        opens = []
        ranges = {}
        for i in range(N):
            if formula[i] == '(':
                opens.append(i)
            if formula[i] == ')':
                ranges[i] = opens.pop()
        elements = [collections.Counter() for _ in range(N)]
        current_el = []
        current_number = []
        i = 0
        while i < N:
            elements[i] = collections.Counter(elements[i - 1])
            c = formula[i]
            if (c.isupper() or c == '(' or c == ')') and len(current_el) > 0:
                last_el = "".join(current_el)
                last_count = 1
                if current_number:
                    last_count = int("".join(current_number))
                counter[last_el] += last_count
                current_el = []
                current_number = []
                elements[i][last_el] += last_count
            if c == '(':
                i += 1
                continue
            if c == ')':
                start = ranges[i]
                to_remove = elements[start] if start > 0 else {}
                current_elements = collections.Counter(elements[i])
                for el, qtd in to_remove.items():
                    if el in current_elements:
                        current_elements[el] -= qtd
                        if current_elements[el] == 0:
                            current_elements.pop(el)
                i += 1
                if i < N:
                    elements[i] = collections.Counter(elements[i - 1])
                last_count = 1
                current_number = []
                should_decrement = False
                while i < N and formula[i].isnumeric():
                    c = formula[i]
                    current_number.append(c)
                    elements[i] = collections.Counter(elements[i - 1])
                    i += 1
                    should_decrement = True
                if should_decrement:
                    i -= 1
                if i < N:
                    elements[i] = collections.Counter(elements[i - 1])
                if current_number:
                    last_count = int("".join(current_number))
                for el, qtd in current_elements.items():
                    counter[el] -= qtd
                    counter[el] += (qtd * last_count)
                    if i < N:
                        elements[i][el] = counter[el]
                current_number = []
                if should_decrement:
                    i += 1
                continue

            if c.isnumeric():
                current_number.append(c)
            else:
                current_el.append(c)
            i += 1
        if len(current_el) > 0:
            last_el = "".join(current_el)
            last_count = 1
            if current_number:
                last_count = int("".join(current_number))
            counter[last_el] += last_count

        ans = []
        atoms = list(counter.keys())
        atoms.sort()
        for atom in atoms:
            if counter[atom] > 1:
                ans.append(atom + str(counter[atom]))
            else:
                ans.append(atom)
        return "".join(ans)


# leetcode submit region end(Prohibit modification and deletion)


class NumberOfAtoms(Solution):
    pass
