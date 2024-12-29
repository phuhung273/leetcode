# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(version: int) -> bool:
    return version >= 1234

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1: return 1

        mid, left, right = 0, 0, n
        while left < right - 1:
            mid = int((left + right) / 2)
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
        result = left if isBadVersion(left) else right
        return result

solution = Solution()
solution.firstBadVersion(1234)