from typing import List


class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) == 1: return 1

        people.sort()
        left, right, result = 0, len(people) - 1, 0
        while left < right:
            result += 1
            
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                continue
            right -= 1

        if left == right:
            result += 1
        return result
        


solution = Solution()
solution.numRescueBoats([2,4], 5) # 2
solution.numRescueBoats([2,2], 3) # 2
solution.numRescueBoats([1,2], 3) # 1
solution.numRescueBoats([3,2,2,1], 3) # 3
solution.numRescueBoats([3,5,3,4], 5) # 4
solution.numRescueBoats([5,1,4,2], 6) # 2