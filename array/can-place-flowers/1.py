from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) < 3:
            return True if (flowerbed.count(1) == 0 and n <= 1) else False

        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue

            if i == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                n -= 1
            elif i == 1 and flowerbed[0] == 0 and flowerbed[2] == 0:
                flowerbed[1] = 1
                n -= 1
            elif i == len(flowerbed) - 1 and flowerbed[len(flowerbed) - 2] == 0:
                flowerbed[len(flowerbed) - 1] = 1
                n -= 1
            elif i == len(flowerbed) - 2 and flowerbed[len(flowerbed) - 1] == 0 and flowerbed[len(flowerbed) - 3] == 0:
                flowerbed[len(flowerbed) - 2] = 1
                n -= 1
            elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1

            if n == 0:
                return True
        
        return False
    
solution = Solution()
# solution.canPlaceFlowers([1,0,0,0,1], 1) # True
# solution.canPlaceFlowers([1,0,0,0,1], 2) # false
# solution.canPlaceFlowers([1,0,1,0,1,0,1], 1) # false
# solution.canPlaceFlowers([1,0,0,0,0,1], 2) # false
# solution.canPlaceFlowers([1,0,0,0,0,0,1], 3) # false
# test=solution.canPlaceFlowers([0], 1) # true
test=solution.canPlaceFlowers([1], 1) # false
print(test)