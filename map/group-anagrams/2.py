"""
Problem: https://leetcode.com/problems/group-anagrams
Idea: Save 2 arrays: results and counters, with counters[i] is counter of results[i]
Time: O(N) with N = num of characters
Space: O(N)
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for str in strs:
            counter = [0] * 26
            for char in str:
                counter[ord(char) - ord('a')] += 1
            ans[tuple(counter)].append(str)
        return list(ans.values())

sol = Solution()
sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
sol.groupAnagrams([""])
sol.groupAnagrams(["a"])
