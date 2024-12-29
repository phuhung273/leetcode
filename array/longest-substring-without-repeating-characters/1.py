class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0

        result, current, start = 0, 0, 0
        indexes = {}
        for end in range(len(s)):
            char = s[end]
            if char not in indexes:
                indexes[char] = end
                current += 1
                result = max(result, current)
                continue

            # Cleanup before
            for i in range(start, indexes[char]):
                del indexes[s[i]]

            start = indexes[char] + 1
            current = end - start + 1
            indexes[char] = end

        return result

solution = Solution()
# solution.lengthOfLongestSubstring('abcabcbb') # 3
# solution.lengthOfLongestSubstring('abcbcbb') # 3
solution.lengthOfLongestSubstring('tmmzuxt') # 5
# solution.lengthOfLongestSubstring('bbbbb') # 1
# solution.lengthOfLongestSubstring('pwwkew') # 3