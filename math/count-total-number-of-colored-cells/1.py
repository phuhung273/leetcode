class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 2 * n * (n - 1)

sol = Solution()
sol.coloredCells(1) # 1
sol.coloredCells(2) # 5
sol.coloredCells(3) # 13
sol.coloredCells(4) # 25