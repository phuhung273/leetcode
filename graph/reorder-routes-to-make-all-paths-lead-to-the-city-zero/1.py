"""
Problem: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero
Idea:
Add all node to 0 to a queue
Also add all node from 0 to this queue, ans += 1 

Pop queue, have i
Add all node to i to queue
Also add all node to i to this queue, ans += 1

Time: O(N)
Space: O(N)
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ans = 0
        q = deque()
        toGraph = defaultdict(set) # to key, we have
        fromGraph = defaultdict(set) # from key, we have

        for u, v in connections:
            toGraph[v].add(u)
            fromGraph[u].add(v)
        
        for i in toGraph[0]:
            q.append(i)
        for i in fromGraph[0]:
            ans += 1
            q.append(i)

        done = set([0])
        
        while q:
            i = q.popleft()
            for u in toGraph[i]:
                if u not in done:
                    q.append(u)
            for v in fromGraph[i]:
                if v not in done:
                    ans += 1
                    q.append(v)
            done.add(i)

        return ans

sol = Solution()
sol.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]) # 3
sol.minReorder(n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]) # 2
sol.minReorder(n = 3, connections = [[1,0],[2,0]]) # 0
