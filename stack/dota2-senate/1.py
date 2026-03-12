"""
Problem: https://leetcode.com/problems/dota2-senate
Idea: Stack
R, [] -> stack = [R], ans = R
D, [R] -> stack = [], ans = R
D, [] -> stack = [D], ans = D

RRRDDDD
stack = [R], ans = R
stack = [R, R], ans = R
stack = [R, R, R], ans = R
stack = [R, R], ans = R
stack = [R], ans = R
stack = [], ans = R
stack = [D], ans = D


RDRDRD
stack = [R], ans = R
stack = [], ans = R
stack = [R], ans = R
stack = [], ans = R
stack = [R], ans = R
stack = [], ans = r

>>> RRRDDDD must be R
--------------------------

Use 2 queues rad and dir. Push index of all items to their respective queue
Compare 2 heads, the higher is pop and eliminated, the lower get push to end of their queue with next index

Time: O(N)
Space: O(N)
"""

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad = deque()
        dir = deque()

        for i, item in enumerate(senate):
            if item == 'R':
                rad.append(i)
            else:
                dir.append(i)
        
        i = len(senate)
        while rad and dir:
            if rad[0] < dir[0]:
                rad.append(i)
            else:
                dir.append(i)
            dir.popleft()
            rad.popleft()
            i += 1

        return "Radiant" if rad else "Dire"

sol = Solution()
sol.predictPartyVictory("DRRD") # D
sol.predictPartyVictory("RD") # R
sol.predictPartyVictory("RDD") # D
sol.predictPartyVictory("RRRDDDD") # R
sol.predictPartyVictory("RDRDRD") # R
