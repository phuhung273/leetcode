"""
Problem: https://leetcode.com/problems/non-overlapping-intervals
Idea: Sort by ascending start, decending end
If current interval overlap, ans += 1

Time: O(sortN)
Space: O(sortN)
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0]))

        ans = 0
        last = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[last][1]:
                ans += 1

                if intervals[i][1] < intervals[last][1]:
                    last = i
            else:
                last = i
        return ans

sol = Solution()
sol.eraseOverlapIntervals([[1,3],[2,3],[3,4],[1,2]]) # 1
sol.eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]) # 2
sol.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]) # 2
sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) # 1
sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) # 2
sol.eraseOverlapIntervals([[1,2],[2,3]]) # 0
