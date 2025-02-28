class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False

        highest1, countMap1, charMap1 = findCharMapAndCountMap(word1)
        highest2, countMap2, charMap2 = findCharMapAndCountMap(word2)

        if highest1 != highest2:
            return False

        for key in charMap1:
            if key not in charMap2:
                return False

        for i in range(1, highest1):
            if countMap1[i] != countMap2[i]:
                return False
        return True

def findCharMapAndCountMap(word):
    highest = 0
    charMap = {}
    countMap = {}
    for char in word:
        count = charMap.get(char, 0) + 1
        countMap[count] = countMap.get(count, 0) + 1
        if count > 1:
            countMap[count - 1] -= 1
        charMap[char] = count
        highest = max(highest, count)
    return highest, countMap, charMap

sol = Solution()
sol.closeStrings('uau', 'ssx') # False
sol.closeStrings('cabbba', 'abbacc') # False
sol.closeStrings('abc', 'bca') # True
sol.closeStrings('aabbcc', 'bbccaa') # True
# sol.closeStrings('a', 'aa') # False
sol.closeStrings('cabbba', 'abbccc') # True