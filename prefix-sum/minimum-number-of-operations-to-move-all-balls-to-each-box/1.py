from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = [0] * len(boxes)

        balls_to_right, moves_to_right = 0, 0
        balls_to_left, moves_to_left = 0, 0
        for i in range(len(boxes)):
            result[i] += balls_to_right + moves_to_right
            moves_to_right += balls_to_right
            if boxes[i] == '1':
                balls_to_right += 1
            
            j = len(boxes) - 1 - i
            result[j] += balls_to_left + moves_to_left
            moves_to_left += balls_to_left
            if boxes[j] == '1':
                balls_to_left += 1

        return result

solution = Solution()
solution.minOperations("110") # [1,1,3]
solution.minOperations("001011") # [11,8,5,4,3,4]