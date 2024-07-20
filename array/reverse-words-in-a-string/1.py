class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 1:
            return s.strip()
        i,j,left,right,resultLeft,resultRight = 0,len(s) - 1,'','',[],[]

        goRight = True

        while i <= j:
            if goRight:
                if s[i] != ' ':
                    left += s[i]
                elif left != '':
                    resultLeft.append(left)
                    left = ''
                    goRight = not goRight
                    continue
                i += 1
            else:
                if s[j] != ' ':
                    right = s[j] + right
                elif right != '':
                    resultRight.append(right)
                    right = ''
                    goRight = not goRight
                    continue
                j -= 1

        if i == len(s):
            return s.strip()

        result = ' '.join(resultRight)
        for i in range(len(resultLeft)):
            result += f" {resultLeft[len(resultLeft) - i - 1]}"
        return result.strip()

solution = Solution()
# solution.reverseWords("the sky is blue") # "blue is sky the"
# solution.reverseWords("  hello world  ") # "world hello"
# solution.reverseWords("  hello  world     test") # "test world hello"
# solution.reverseWords("  hello  word     test") # "test world hello"
# solution.reverseWords("EPY2giL") # "test world hello"
t = solution.reverseWords(" t") # "test world hello"
t = solution.reverseWords("t ") # "test world hello"
print("test")