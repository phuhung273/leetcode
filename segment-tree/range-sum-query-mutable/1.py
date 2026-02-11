"""
Problem: https://leetcode.com/problems/range-sum-query-mutable/
Time:
- init: O(N)
- update: O(logN)
- query: O(logN)
Space: O(N)
"""

from typing import List


class SegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * 4 * self.n
        self.__build__(nums, 0, self.n - 1, 0)

    def __build__(self, nums: List[int], left, right, index: int):
        if left == right:
            self.tree[index] = nums[left]
            return
        
        mid = (left + right) // 2
        self.__build__(nums, left, mid, 2 * index + 1)
        self.__build__(nums, mid + 1, right, 2 * index + 2)
        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]
    
    def querySum(self, index, left, right, qLeft, qRight) -> int:
        # No overlap
        if left > qRight or right < qLeft:
            return 0
        # Full overlap
        if left >= qLeft and right <= qRight:
            return self.tree[index]
        # Partial overlap
        mid = (left + right) // 2
        return self.querySum(2 * index + 1, left, mid, qLeft, qRight) \
            + self.querySum(2 * index + 2, mid + 1, right, qLeft, qRight)
    
    def update(self, index, pos, diff, left, right):
        if pos < left or pos > right:
            return
        self.tree[index] += diff

        if left != right:
            mid = (left + right) // 2
            self.update(2 * index + 1, pos, diff, left, mid)
            self.update(2 * index + 2, pos, diff, mid + 1, right)
        

class NumArray:

    def __init__(self, nums: List[int]):
        self.segmentTree = SegmentTree(nums)
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self.segmentTree.update(0, index, diff, 0 , len(self.nums) - 1)

    def sumRange(self, left: int, right: int) -> int:
        return self.segmentTree.querySum(0, 0, len(self.nums) - 1, left, right)

obj = NumArray([7,2,7,2,0])
obj.update(4, 6)
obj.update(0, 2)
obj.update(0, 9)
obj.sumRange(4, 4)
obj.update(3, 8)
obj.sumRange(0, 4)
obj.update(4, 1)
obj.sumRange(0, 3)
obj.sumRange(0, 4)
obj.update(0, 4)

obj = NumArray([1, 3, 5])
obj.update(1, 10)
obj.sumRange(0, 2)
obj.sumRange(0, 1)
obj.sumRange(1, 2)
