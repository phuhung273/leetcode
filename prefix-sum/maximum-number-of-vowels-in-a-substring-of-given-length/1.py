from collections import deque

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        result = 0
        current = 0
        queue = deque()

        for i in range(len(s)):
            char = s[i]
            queue.append(char)

            if isVowel(char):
                current += 1
                result = max(result, current)

            if i < k - 1:
                continue

            if isVowel(queue[0]):
                current -= 1
            queue.popleft()

        return result

def isVowel(char):
    return char in { 'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}

sol = Solution()
sol.maxVowels('abciiidef', 3) # 3
sol.maxVowels('aeiou', 2) # 2
sol.maxVowels('leetcode', 3) # 2
sol.maxVowels('aeiou', 1) # 1