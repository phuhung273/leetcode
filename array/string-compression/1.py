"""
Problem: https://leetcode.com/problems/string-compression
Idea: Save a lastChar, count and writeIndex.
Append number: count // 10
8765

Time: O(N)
Space: O(1)
"""

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        lastChar = chars[0]
        count = 0
        writeIndex = 0

        def write():
            nonlocal count, writeIndex
            if count == 1:
                return
            powerOfTen = 0
            while count >= 10**powerOfTen:
                powerOfTen += 1
            newWriteIndex = writeIndex + powerOfTen
            while count > 0:
                chars[writeIndex + powerOfTen - 1] = str(count % 10)
                count //= 10
                powerOfTen -= 1
            count = 1
            writeIndex = newWriteIndex

        for char in chars:
            if char != lastChar:
                chars[writeIndex] = lastChar
                writeIndex += 1
                lastChar = char
                if count == 1:
                    continue
                write()
                continue
            count += 1
        
        chars[writeIndex] = lastChar
        writeIndex += 1
        write()

        return writeIndex

sol = Solution()
sol.compress(["o","o","o","o","o","o","o","o","o","o"])
sol.compress(["a","a","a","b","b","a","a"])
sol.compress(["a","a","b","b","c","c","c"])
sol.compress(["a"])
sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
