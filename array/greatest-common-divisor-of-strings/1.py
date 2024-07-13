class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        short_len = min(len(str1), len(str2))
        len1, len2 = len(str1), len(str2)
        for i in range(short_len):
            if str1[i] == str2[i]:
                continue
            return ''
        
        if len2 < len1:
            remaining = str1[short_len:]
            if str2 == remaining:
                return remaining
            return self.gcdOfStrings(str2, remaining)
        elif len1 < len2:
            remaining = str2[short_len:]
            if str1 == remaining:
                return remaining
            return self.gcdOfStrings(str1, remaining)
        else:
            return str1
        
        
solution = Solution()
solution.gcdOfStrings("ABCABC", "ABC") # ABC
solution.gcdOfStrings("ABABAB", "ABAB") # AB
solution.gcdOfStrings("ABABABAB", "ABAB") # ABAB
solution.gcdOfStrings("ABABABAB", "ABABC") # ABAB
solution.gcdOfStrings("LEET", "CODE") # ''