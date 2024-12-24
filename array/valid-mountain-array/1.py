from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # Early return
        if len(arr) < 3 or arr[1] <= arr[0]:
            return False

        isIncreasing = True
        index = 1
        
        while index < len(arr):
            if arr[index] == arr[index - 1]:
                return False

            # Upward
            if isIncreasing and arr[index] < arr[index - 1]:
                isIncreasing = False
            # Downward
            elif not isIncreasing and arr[index] > arr[index - 1]:
                return False
            index = index + 1
        return not isIncreasing

solution = Solution()
solution.validMountainArray([2,1]) # false
solution.validMountainArray([3,5,5]) # false
solution.validMountainArray([0,3,2,1]) # true
solution.validMountainArray([0,2,3,4,5,2,1,0]) # true
solution.validMountainArray([0,2,3,4,5,2,1,1]) # false
solution.validMountainArray([0,2,3,3,5,2,1,0]) # false