"""
Problem: https://leetcode.com/problems/evaluate-division
Idea:
a/b = a/c * c/b = a/d * d/c * c/b
Build a map of: {
    a: {
        c: 2
        b: 1
    },
    c: {
        d: 3
        b: 1
    }
}
Then DFS to find the answer, stop if see 0. During traversal, multiply to current.
If found, add to the graph
If not found, add 0

Time:
Space:
"""

from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ans = [-1.0] * len(queries)
        graph = defaultdict(dict)

        for i, (first, second) in enumerate(equations):
            graph[first][second] = values[i]
            graph[second][first] = 1 / values[i]

        curr = 1.0
        done = set()

        def dfs(node, target: str):
            nonlocal curr
            if node == target:
                return curr

            
            for second in graph[node]:
                if second in done:
                    continue
                elif graph[node][second] == 0:
                    continue

                done.add(second)
                curr *= graph[node][second]
                val = dfs(second, target)
                done.remove(second)

                if val != -1.0:
                    return val
                curr /= graph[node][second]
            
            return -1.0

        for i, (first, second) in enumerate(queries):
            curr = 1.0
            if first not in graph or second not in graph:
                ans[i] = -1.0
            elif first == second:
                ans[i] = 1.0
            else:
                done.add(first)
                ans[i] = dfs(first, second)
                done.remove(first)

                if ans[i] != -1:
                    graph[first][second] = ans[i]
                    graph[second][first] = 1 / ans[i]
                else:
                    graph[first][second] = 0
                    graph[second][first] = 0
            
        return ans

sol = Solution()
sol.calcEquation(equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], values = [3.0,4.0,5.0,6.0], queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]])
sol.calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
sol.calcEquation(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]])
sol.calcEquation(equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]])
