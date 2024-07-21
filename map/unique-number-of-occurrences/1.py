from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurs = {}
        for num in arr:
            occurs[num] = occurs[num] + 1 if num in occurs else 1
        final = {}
        for occur in occurs.values():
            if occur in final:
                return False
            final[occur] = 1
        return True
    
solution = Solution()
solution.uniqueOccurrences([1,2,2,1,1,3]) # true
solution.uniqueOccurrences([1,2]) # false
solution.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]) # true