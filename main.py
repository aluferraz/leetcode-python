from leetcode.editor.en.Q432.AllOoneDataStructure import AllOoneDataStructure

if __name__ == '__main__':
    # print(SumOfPrefixScoresOfStrings().sumPrefixScores(["abc", "ab", "bc", "b"]))
    obj = AllOoneDataStructure()
    obj.inc("hello")
    obj.inc("hello")
    print(obj.getMaxKey())
    print(obj.getMinKey())
    obj.inc("leet")
    print(obj.getMaxKey())
    print(obj.getMinKey())
