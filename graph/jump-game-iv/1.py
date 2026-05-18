"""
Problem: https://leetcode.com/problems/jump-game-iv
Idea:
Build a graph and BFS with a queue.
---
DP
dp[i] = min(dp[i + 1], dp[i - 1], dp[map[arr[i]]]) + 1
> Not sure how to find map[arr[i]]
Time:
Space:
"""

from collections import deque
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        duplicateMap = {}

        for i, num in enumerate(arr):
            if num not in duplicateMap:
                duplicateMap[num] = set()
            duplicateMap[num].add(i)

        q = deque()
        q.append((0, 0))

        def addToQueue(i: int, distance: int):
            visited.add(i)
            q.append((distance, i))

        ans = len(arr) - 1
        visited = set([0])

        while q:
            distance, i = q.popleft()

            if distance > ans:
                break

            if i == len(arr) - 1:
                ans = min(ans, distance)
                continue

            if i - 1 not in visited and i > 0:
                addToQueue(i - 1, distance + 1)

            if i + 1 not in visited and i + 1 < len(arr):
                addToQueue(i + 1, distance + 1)

            if arr[i] not in duplicateMap:
                continue

            for j in duplicateMap[arr[i]]:
                if j in visited:
                    continue
                addToQueue(j, distance + 1)
                if j == len(arr) - 1:
                    break

            del duplicateMap[arr[i]]

        return ans

sol = Solution()
sol.minJumps([7,7,7,7,11]) # 2
sol.minJumps([7,7,7,7,7,7,7,7,7,7,7,7]) # 1
sol.minJumps([7,7,2,1,7,7,7,3,4,1]) # 3
sol.minJumps([100,-23,-23,404,100,23,23,23,3,404]) # 3
sol.minJumps([7]) # 0
sol.minJumps([7,6,9,6,9,6,9,7]) # 1
