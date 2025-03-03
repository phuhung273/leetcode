from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = {}

        stack = [rooms[0]]
        while stack:
            keys = stack.pop()

            for key in keys:
                if key not in graph:
                    graph[key] = True
                    stack.append(rooms[key])
        
        for i in range(1, len(rooms)):
            if i not in graph:
                return False
        return True

sol = Solution()
sol.canVisitAllRooms([[1],[2],[3],[]]) # true
sol.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]) # false