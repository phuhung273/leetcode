"""
Problem: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays
Idea:
During iteration, store numbers in A and B to a map.
For next iteration, if A = B + 1 -> +1, if B = A + 1 -> also +1
Time: O(N)
Space: O(N)
"""

from typing import Counter, List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        counterA = Counter()
        counterB = Counter()
        ans = [0] * len(A)
        ans[0] = 1 if A[0] == B[0] else 0
        counterA[A[0]] += 1
        counterB[B[0]] += 1

        for i in range(1, len(A)):
            ans[i] = ans[i - 1]

            if A[i] == B[i]:
                ans[i] += 1
                continue

            counterA[A[i]] += 1
            counterB[B[i]] += 1

            if counterB[B[i]] == counterA[B[i]]:
                ans[i] += 1
            if counterB[A[i]] == counterA[A[i]]:
                ans[i] += 1

        return ans

sol = Solution()
sol.findThePrefixCommonArray(A = [0,0,0,1], B = [1,0,0,0]) # [0,1,2,4]
sol.findThePrefixCommonArray(A = [1,3,2,4], B = [3,1,2,4]) # [0,2,3,4]
sol.findThePrefixCommonArray(A = [2,3,1], B = [3,1,2]) # [0,1,3]
