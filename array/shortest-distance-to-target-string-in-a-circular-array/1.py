"""
Problem: https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array
Idea: When found, return min(i - startIndex, startIndex + n - i)
Bug: handle duplicate, when found, do not return immediately
Time: O(N)
Space: O(1)
"""

import math
from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans = math.inf

        for i, word in enumerate(words):
            if word != target:
                continue
            if i == startIndex:
                return 0
            elif i < startIndex:
                ans = min(ans, min(startIndex - i, i + len(words) - startIndex))
            else:
                ans = min(ans, min(i - startIndex, len(words) + startIndex - i))
        return int(ans) if ans != math.inf else -1

sol = Solution()
sol.closestTarget(words = ["hsdqinnoha","mqhskgeqzr","zemkwvqrww","zemkwvqrww","daljcrktje","fghofclnwp","djwdworyka","cxfpybanhd","fghofclnwp","fghofclnwp"], target = "zemkwvqrww", startIndex = 8) # 4
sol.closestTarget(words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1) # 1
sol.closestTarget(words = ["a","b","leetcode"], target = "leetcode", startIndex = 0) # 1
sol.closestTarget(words = ["i","eat","leetcode"], target = "ate", startIndex = 0) # -1
