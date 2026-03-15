"""
Problem: https://leetcode.com/problems/fancy-sequence
Idea:
Store 1 arrays with item (1/0, inc/mul, length at that time). 1 is add, 0 is mult
When getIndex, do the calculation
Time:
append: O(1)
addAll: O(1)
multAll: O(1)
getIndex: O(add + mult)
Space: O(N)

---

+1, x3 --> newVal = valx3 + 3
Add
+2, x4
Before: newVal = valx12 + 20
After: newVal = valx4 + 8
+5, x10 --> newVal = valx120 + 250

"""

ADD = 1
MUL = 0
MOD = 10**9 + 7

class Fancy:

    def __init__(self):
        self.arr = []
        self.muls = [(-1, 1)]
        self.adjustedSums = [(-1, 0)]
        self.cache = {}

    def append(self, val: int) -> None:
        self.arr.append(val)

    def addAll(self, inc: int) -> None:
        self.adjustedSums.append((len(self.arr) - 1, self.adjustedSums[-1][1] + inc))
        self.cache = {}

    def multAll(self, m: int) -> None:
        self.muls.append((len(self.arr) - 1, self.muls[-1][1] * m))
        self.adjustedSums.append((len(self.arr) - 1, self.adjustedSums[-1][1] * m))
        self.cache = {}

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        if idx in self.cache:
            return self.cache[idx]

        ans = self.arr[idx]
        currMul = 1
        for i in range(len(self.muls) - 1, -1, -1):
            if self.muls[i][0] < idx:
                currMul = self.muls[-1][1] // self.muls[i][1]
                ans *= currMul
                break
        ans %= MOD

        for i in range(len(self.adjustedSums) - 1, -1, -1):
            if self.adjustedSums[i][0] < idx:
                ans -= self.adjustedSums[i][1] * currMul
                break
        ans += self.adjustedSums[-1][1]
        ans %= MOD
        self.cache[idx] = ans
        return ans

# fancy = Fancy()
# fancy.append(3)
# fancy.multAll(10)
# fancy.append(3)
# fancy.multAll(2)
# fancy.getIndex(1)
# fancy.multAll(8)
# fancy.getIndex(6)
# fancy.multAll(7)
# fancy.append(3)
# fancy.append(6)
# fancy.append(7)
# fancy.multAll(4)
# fancy.getIndex(3)
# fancy.append(3)
# fancy.multAll(7)
# fancy.multAll(3)
# fancy.addAll(6)
# fancy.multAll(10)
# fancy.multAll(8)
# fancy.multAll(8)
# fancy.getIndex(5)
# fancy.append(7)
# fancy.append(7)
# fancy.addAll(3)
# fancy.getIndex(4)
# fancy.getIndex(0)
# fancy.multAll(5)
# fancy.getIndex(0)
# fancy.getIndex(4)
# fancy.getIndex(7)

# Your Fancy fancyect will be instantiated and called as such:
fancy = Fancy()
fancy.append(2)   # fancy sequence: [2]
fancy.addAll(3)   # fancy sequence: [2+3] -> [5]
fancy.append(7)   # fancy sequence: [5, 7]
fancy.multAll(2)  # fancy sequence: [5*2, 7*2] -> [10, 14]
fancy.getIndex(0) # return 10
fancy.addAll(3)   # fancy sequence: [10+3, 14+3] -> [13, 17]
fancy.append(10)  # fancy sequence: [13, 17, 10]
fancy.multAll(2)  # fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
fancy.getIndex(0) # return 26
fancy.getIndex(1) # return 34
fancy.getIndex(2) # return 20
fancy.append(5)   # fancy sequence: [26, 34, 20, 5]
fancy.addAll(5)   # fancy sequence: [31, 39, 25, 10]
fancy.multAll(3)   # fancy sequence: [93, 117, 75, 30]
fancy.getIndex(0) # return 93
fancy.getIndex(1) # return 117
fancy.getIndex(2) # return 75
fancy.getIndex(3) # return 30
