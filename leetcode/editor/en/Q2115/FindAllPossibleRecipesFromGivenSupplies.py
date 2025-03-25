from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipes_ingredients = {}
        N = len(recipes)
        for i in range(N):
            recipes_ingredients[recipes[i]] = set(ingredients[i])

        done = set()
        can_bake = True
        while can_bake:
            can_bake = False
            for r, ing in recipes_ingredients.items():
                if r in done:
                    continue
                for sup in supplies:
                    ing.discard(sup)
                if len(ing) == 0:
                    supplies.append(r)
                    done.add(r)
                    can_bake = True
        return list(done)


# leetcode submit region end(Prohibit modification and deletion)


class FindAllPossibleRecipesFromGivenSupplies(Solution):
    pass
