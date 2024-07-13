class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max1, max2 = len(word1), len(word2)
        i,j = 0,0
        result = ''

        while i < max1 or j < max2:
            if i == max1:
                result += word2[j]
                j += 1
            elif j == max2:
                result += word1[i]
                i += 1
            else:
                if i <= j:
                    result += word1[i]
                    i += 1
                else:
                    result += word2[j]
                    j += 1
        return result
        
solution = Solution()
solution.mergeAlternately("abc", "pqr") # apbqcr
solution.mergeAlternately("ab", "pqrs") # apbqrs
solution.mergeAlternately("abcd", "pq") # apbqcd