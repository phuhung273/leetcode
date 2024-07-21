from typing import List
import sys

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        elif len(nums) == 3:
            if nums[0] < nums[1] < nums[2]:
                return True
            else: 
                return False

        minimum,maximum = nums[0], sys.maxsize

        for num in nums:
            if num < minimum:
                minimum = num
            elif num < maximum and num > minimum:
                maximum = num
            elif num > maximum:
                return True
        return False

sol = Solution()
sol.increasingTriplet([1,2,3]) # true
sol.increasingTriplet([1,2,3,4,5]) # true
sol.increasingTriplet([5,4,3,2,1]) # false
sol.increasingTriplet([2,1,5,0,4,6]) # true
sol.increasingTriplet([2,1,5,3,4]) # true
sol.increasingTriplet([5,3,4,5]) # true
sol.increasingTriplet([5,3,4,4]) # false
sol.increasingTriplet([2,1,5,-2,-1,0]) # true