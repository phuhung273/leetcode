"""
Problem: https://leetcode.com/problems/champagne-tower
Idea: DP

f is amount of wine flow through (row, glass)
f(row, glass) = f(row - 1, glass) / 2 + f(row - 1, glass - 1) / 2

                        25
                    12      12
                5.5     11      5.5
            2.25    7.25    7.25    2.25
        0.625   3.75    6.25    3.75    0.625

Time: O(query_row^2)
Space: O(query_row)
"""


from functools import cache


class Solution:
    # # Top down
    # def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
    #     if poured == 0:
    #         return 0
    #     elif poured == 1:
    #         return 1 if query_row == 0 else 0

    #     @cache
    #     def pour(query_row: int, query_glass: int) -> float:
    #         nonlocal poured

    #         # Base case
    #         if query_row == 0:
    #             return poured

    #         amount = 0
    #         if query_glass != query_row:
    #             upper = pour(query_row - 1, query_glass)
    #             if upper > 1:
    #                 amount += (upper - 1) / 2
    #         if query_glass != 0:
    #             upper = pour(query_row - 1, query_glass - 1)
    #             if upper > 1:
    #                 amount += (upper - 1) / 2
    #         return amount
        
    #     ans = pour(query_row, query_glass)
    #     if ans > 1:
    #         return 1
    #     elif ans < 0:
    #         return 0
    #     return ans
    
    # Bottom up
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        lastDp = [0] * (query_row + 1)
        lastDp[0] = poured
        for row in range(1, query_row + 1):
            isEnough = False
            dp = [0.0] * (query_row + 1)
            for col in range(row + 1):
                if col < row:
                    if lastDp[col] > 1:
                        isEnough = True
                        dp[col] += (lastDp[col] - 1) / 2
                if col > 0:
                    if lastDp[col - 1] > 1:
                        isEnough = True
                        dp[col] += (lastDp[col - 1] - 1) / 2
            if not isEnough:
                return 0
            lastDp = dp
        return lastDp[query_glass] if lastDp[query_glass] < 1 else 1


sol = Solution()
sol.champagneTower(25, 6, 1) # 0.1875
sol.champagneTower(100000009, 33, 17) #
sol.champagneTower(4, 0, 0) # 1
sol.champagneTower(4, 1, 0) # 1
sol.champagneTower(4, 1, 1) # 1
sol.champagneTower(2, 1, 0) # 0.5
sol.champagneTower(3, 1, 1) # 1
sol.champagneTower(4, 2, 1) # 0.5
sol.champagneTower(1, 1, 1) # 0
sol.champagneTower(2, 1, 1) # 0.5
