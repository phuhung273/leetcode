from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        exist1, exist2 = {},{}
        result1, result2 = set(),set()
        for num in nums1:
            exist1[num] = 1

        for num in nums2:
            exist2[num] = 1
            if num not in exist1:
                result2.add(num)
        
        for num in nums1:
            if num not in exist2:
                result1.add(num)
        return [list(result1), list(result2)]
    
solution = Solution()
# solution.findDifference([1,2,3], [2,4,6]) # [[1,3],[4,6]]
# solution.findDifference([1,2,3,3], [1,1,2,2]) # [[3],[]]
solution.findDifference([-80,-15,-81,-28,-61,63,14,-45,-35,-10], [-1,-40,-44,41,10,-43,69,10,2]) # [[-80,-15,-81,-28,-61,63,14,-45,-35,-10],[-1,-40,-44,41,10,-43,69,10,2]]