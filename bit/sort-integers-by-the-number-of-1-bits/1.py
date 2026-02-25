"""
Problem: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits
Idea: Sort array > Add to a map with key as their set bits
Time: O(sortN)
Space: O(N)
"""

from collections import defaultdict
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        bitCountMap = defaultdict(list)

        for num in arr:
            bitCountMap[num.bit_count()].append(num)
        
        i = 0
        for bitCount in range(33):
            for num in bitCountMap[bitCount]:
                arr[i] = num
                i += 1

        return arr

sol = Solution()
sol.sortByBits([0,1,2,3,4,5,6,7,8])
sol.sortByBits([1024,512,256,128,64,32,16,8,4,2,1])
