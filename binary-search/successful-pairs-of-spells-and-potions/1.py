import bisect
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        result = []

        for spell in spells:
            index = bisect.bisect_left(potions, success / spell)
            result.append(len(potions) - index)

        return result

sol = Solution()
sol.successfulPairs([5,1,3], [1,2,3,4,5], 7) # [4,0,3]
sol.successfulPairs([3,1,2], [8,5,8], 16) # [2,0,2]