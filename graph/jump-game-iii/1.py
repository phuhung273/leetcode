"""
Problem: https://leetcode.com/problems/jump-game-iii
Idea: Build a graph of fromIndex: [toIndex]
Find all indexes of 0
Traverse the graph DFS to check if there is a way from index of 0 to start
Time: O(N)
Space: O(N)
"""

from collections import defaultdict
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        graph = defaultdict(set)

        for i, val in enumerate(arr):
            if val == 0:
                continue

            right = i + val
            left = i - val
            if right < len(arr):
                graph[i].add(right)
            if left > -1:
                graph[i].add(left)
        
        visited = set()

        def dfs(i: int) -> bool:
            if arr[i] == 0:
                return True
            
            visited.add(i)

            for j in graph[i]:
                if j in visited:
                    continue

                if dfs(j):
                    return True

            return False

        ans = dfs(start)
        return ans

sol = Solution()
# sol.canReach(arr = [0,3,0,6,3,3,4], start = 6) # T
# sol.canReach(arr = [4,2,3,0,3,1,2], start = 5) # T
# sol.canReach(arr = [4,2,3,0,3,1,2], start = 0) # T
sol.canReach(arr = [3,0,2,1,2], start = 2) # F
