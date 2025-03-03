from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, equal, greater = [], [], []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)

        less.extend(equal)
        less.extend(greater)
        return less

sol = Solution()
sol.pivotArray([9,12,5,10,14,3,10], 10) # [9,5,3,10,10,12,14]
sol.pivotArray([-3,4,3,2], 2) # [-3,2,4,3]