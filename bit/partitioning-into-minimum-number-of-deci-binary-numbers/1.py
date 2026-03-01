"""
Problem: https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers
Idea: For every iteration, ans = max(arr[i], ans)
Stop when ans==9 > Is this correct. Yes as 9*1 cannot increase next digit
Time: O(N)
Space: O(1)
"""

class Solution:
    def minPartitions(self, n: str) -> int:
        ans = 0
        for i in range(len(n)):
            ans = max(int(n[i]), ans)
            if ans == 9:
                break
        return ans

sol = Solution()
sol.minPartitions("279") # 111*2 + 11*5 + 2*1
sol.minPartitions("32")
sol.minPartitions("82734")
sol.minPartitions("27346209830709182346")
