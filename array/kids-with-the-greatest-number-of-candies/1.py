from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        return [True if x >= greatest - extraCandies else False for x in candies]

solution = Solution()
solution.kidsWithCandies([2,3,5,1,3], 3) # [true,true,true,false,true]
solution.kidsWithCandies([4,2,1,1,2], 1) # [true,false,false,false,false]
solution.kidsWithCandies([12,1,12], 10) # [true,false,true]