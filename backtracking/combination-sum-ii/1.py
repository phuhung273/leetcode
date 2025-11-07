"""
Problem: https://leetcode.com/problems/combination-sum-ii/
Idea: Sort and Backtrack
Time:
Space:
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = []
        candidates.sort()
        pos = {}
        for i, candidate in enumerate(candidates):
            if candidate not in pos:
                pos[candidate] = i

        def choose(i: int):
            if sum(curr) == target:
                ans.append(curr.copy())
                return
            elif sum(curr) > target:
                return

            last = None
            for j in range(i, len(candidates)):
                if last != None and last == candidates[j]:
                    continue
                last = candidates[j]
                curr.append(candidates[j])
                choose(j + 1)
                curr.pop()

        for i in pos.values():
            curr = [candidates[i]]
            choose(i + 1)
        return ans

sol = Solution()
sol.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8)
sol.combinationSum2(candidates = [2,5,2,1,2], target = 5)
sol.combinationSum2(candidates = [2,1,1], target = 2)
