from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]
    
solution = Solution()
solution.findDifference([1,2,3], [2,4,6]) # [[1,3],[4,6]]
# solution.findDifference([1,2,3,3], [1,1,2,2]) # [[3],[]]
# solution.findDifference([-80,-15,-81,-28,-61,63,14,-45,-35,-10], [-1,-40,-44,41,10,-43,69,10,2]) # [[-80,-15,-81,-28,-61,63,14,-45,-35,-10],[-1,-40,-44,41,10,-43,69,10,2]]