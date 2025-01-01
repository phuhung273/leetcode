class Solution:
    def maxScore(self, s: str) -> int:
        left = 1 if s[0] == '0' else 0
        result = left
        for i in range(1, len(s)):
            if s[i] == '1':
                result += 1
        tempResult = result
        for i in range(1, len(s) - 1):
            if s[i] == '1':
                tempResult -= 1
                continue
            tempResult += 1
            result = max(result, tempResult)

        return result

solution = Solution()
solution.maxScore('011101') # 5
solution.maxScore('00111') # 5
solution.maxScore('1111') # 3
solution.maxScore('00001111') # 8
solution.maxScore('0111000001') # 7
solution.maxScore('011100000') # 5