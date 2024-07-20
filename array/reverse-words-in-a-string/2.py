class Solution:
    def reverseWords(self, s: str) -> str:
        result, current = '', ''
        for char in s:
            if char != ' ':
                current += char
            elif current != '':
                if result == '':
                    result = current
                else:
                    result = current + f' {result}'
                current = ''
        if current != '':
            if result == '':
                    result = current
            else:
                result = current + f' {result}'
        return result

solution = Solution()
solution.reverseWords("the sky is blue") # "blue is sky the"
solution.reverseWords("  hello world  ") # "world hello"
solution.reverseWords("  hello  world     test") # "test world hello"
solution.reverseWords("  hello  word     test") # "test world hello"
solution.reverseWords("EPY2giL") # "EPY2giL"
t = solution.reverseWords(" t") # "t"
t = solution.reverseWords("t ") # "t"
print("test")