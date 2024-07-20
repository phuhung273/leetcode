class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = { x: 1 for x in ['a', 'e', 'i', 'o', 'u'] }
        i,j = 0, len(s) - 1

        result = list(s)
        while i < j:
            if result[i].lower() in vowels and result[j].lower() in vowels:
                result[i],result[j] = result[j],result[i]
                j -= 1
                i += 1
            elif result[i].lower() in vowels:
                j -= 1
            else:
                i += 1
        return ''.join(result)
    
solution = Solution()
solution.reverseVowels("hello") # "holle"
solution.reverseVowels("leetcode") # "leotcede"