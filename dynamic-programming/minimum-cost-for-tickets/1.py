from typing import List
import math

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        results = [math.inf] * days[len(days) - 1]

        dayMap = {
            0: 1,
            1: 7,
            2: 30,
        }
        includedDays = {}
        for day in days:
            includedDays[day] = True
        lastResult = 0

        for i in range(len(costs)):
            cost = costs[i]
            dayRange = dayMap[i]
            for day in range(len(results)):
                if day <= dayRange - 1:
                    if day + 1 not in includedDays and i == 0:
                        results[day] = 0
                        continue
                    results[day] = min(results[day], cost)
                else:
                    if day + 1 not in includedDays:
                        results[day] = min(lastResult, results[day])
                        continue

                    for j in range(i + 1):
                        lastNDayResult = results[day - dayMap[j]]
                        results[day] = min(lastNDayResult + costs[j], results[day])
                lastResult = results[day]

        return lastResult

solution = Solution()
# solution.mincostTickets([1,4,6,7,8,20], [2,7,15]) # 11
# solution.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]) # 17
solution.mincostTickets([6,8,9,18,20,21,23,25], [2,10,41]) # 17