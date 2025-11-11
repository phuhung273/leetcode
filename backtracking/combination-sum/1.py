"""
Problem: https://leetcode.com/problems/combination-sum

Idea: Backtrack with current contains frequency of num
For each position, try frequency in range 0:(target // num + 1)

Time: O((target // min)^N)

Space: O(N) = N(current) + N * 2(input var i + local var j)
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        current_solution = []
        current_sum = 0

        def choose(i: int):
            nonlocal current_sum
            if current_sum == target:
                tmp = []
                for i, freq in enumerate(current_solution):
                    tmp.extend([candidates[i]] * freq)
                ans.append(tmp)
                return
            elif current_sum > target or len(current_solution) >= len(candidates) or i >= len(candidates):
                return
            
            for j in range((target - current_sum) // candidates[i] + 1):
                current_solution.append(j)
                current_sum += candidates[i] * j
                choose(i + 1)
                current_solution.pop()
                current_sum -= candidates[i] * j
            return

        choose(0)
        return ans
        
sol = Solution()
sol.combinationSum(candidates = [2,3,6,7], target = 7)
sol.combinationSum(candidates = [2,3,5], target = 8)
sol.combinationSum(candidates = [2], target = 1)
