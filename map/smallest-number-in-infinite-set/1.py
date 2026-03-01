"""
Problem: https://leetcode.com/problems/smallest-number-in-infinite-set
Idea:
- Init: save a removedSet, smallest = 1
- addBack: if not in removedSet, skip. If yes, remove from removedSet. If smaller than smallest, smallest = num
- popSmallest: add smallest to removedSet, increment to find next smallest by checking removedSet
Time:
Space:
"""

class SmallestInfiniteSet:

    def __init__(self):
        self.removed = set()
        self.smallest = 1
        

    def popSmallest(self) -> int:
        res = self.smallest
        self.removed.add(self.smallest)

        newSmallest = self.smallest + 1
        while newSmallest in self.removed:
            newSmallest += 1
        self.smallest = newSmallest

        return res
        

    def addBack(self, num: int) -> None:
        if num not in self.removed:
            return
        self.removed.remove(num)
        if num < self.smallest:
            self.smallest = num
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
obj = SmallestInfiniteSet()
obj.addBack(2)
obj.popSmallest() # 1
obj.popSmallest() # 2
obj.popSmallest() # 3
obj.addBack(1)
obj.popSmallest() # 1
obj.popSmallest() # 4
obj.popSmallest() # 5