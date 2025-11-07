"""
Idea: Backtrack with marker and the 4 adjacent cells as options
Time:
Space:
"""

from functools import cache
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])
        current = ''

        def choose(y, x: int) -> bool:
            nonlocal current

            if current + board[y][x] == word:
                return True
            elif len(current) >= len(word):
                return False
            elif board[y][x] != word[len(current)]:
                return False

            current += board[y][x]
            board[y][x] = ''

            # Left
            if  x > 0 and board[y][x-1] and choose(y, x - 1):
                return True
            # Right
            if  x < width - 1 and board[y][x+1] and choose(y, x + 1):
                return True
            # Up
            if  y > 0 and board[y-1][x] and choose(y - 1, x):
                return True
            # Down
            if  y < height - 1 and board[y+1][x] and choose(y + 1, x):
                return True

            board[y][x] = current[len(current) - 1]
            current = current[:-1]
            return False

        for y in range(len(board)):
            for x in range(len(board[0])):
                if choose(y, x):
                    return True
        return False

sol = Solution()
sol.exist(board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]], word = "BBAAAAAAAAAAAAA") # True
sol.exist(board = [["a"]], word = "a") # True
sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED") # True
sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE") # True
sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB") # False
print('hello')
