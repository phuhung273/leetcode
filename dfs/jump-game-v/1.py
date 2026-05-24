"""
Problem: https://leetcode.com/problems/jump-game-v
Idea:
Observations: we should jump to index with more children (lower than itself)
> Build a graph of parent: [children] by iterating and check [i-d, i] and [i, i+d] > O(N*D), if encountering >=, break

Iterate and DFS each index to find max steps with cache
Time: O(ND)
Space: O(ND)
"""

from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        graph = defaultdict(set)

        for i in range(n):
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break
                graph[i].add(j)
            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]:
                    break
                graph[i].add(j)

        ans = 0

        @cache
        def dfs(i: int) -> int:
            if len(graph[i]) == 0:
                return 0

            tempAns = 0

            for j in graph[i]:
                tempAns = max(tempAns, dfs(j))

            return tempAns + 1

        for i in range(n):
            ans = max(ans, dfs(i) + 1)

        return ans

sol = Solution()
sol.maxJumps(arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2) # 4
sol.maxJumps(arr = [3,3,3,3,3], d = 3) # 1
sol.maxJumps(arr = [7,6,5,4,3,2,1], d = 1) # 7
