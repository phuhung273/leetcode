from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = []
        results = []
        for str in strs:
            currentMap = {}
            for char in str:
                currentMap[char] = 1 if char not in currentMap else currentMap[char] + 1
            
            found = False
            for i in range(len(maps)):
                existingMap = maps[i]
                if self.isSameMap(existingMap, currentMap):
                    results[i].append(str)
                    found = True
                    break
            
            if not found:
                results.append([str])
                maps.append(currentMap)
        return results
    
    def isSameMap(self, a, b) -> bool:
        if len(a) != len(b): return False

        same = True
        for key in a:
            if key not in b or a[key] != b[key]:
                same = False
                break
        return same

solution = Solution()
solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
solution.groupAnagrams([""])
solution.groupAnagrams(["a"])