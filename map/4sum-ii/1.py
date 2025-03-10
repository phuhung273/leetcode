from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        result = 0
        cache = {}
        for num in nums4:
            if num in cache:
                result += cache[num]
                continue

            count = self.threeSumCount(target=-num, nums1=nums1, nums2=nums2, nums3=nums3)
            cache[num] = count
            result += count
        return result
    
    def threeSumCount(self, target: int, nums1: List[int], nums2: List[int], nums3: List[int]) -> int:
        result = 0
        cache = {}
        for num in nums3:
            if num in cache:
                result += cache[num]
                continue

            count = self.twoSumCount(target=target - num, nums1=nums1, nums2=nums2)
            cache[num] = count
            result += count
        return result
    
    def twoSumCount(self, target: int, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        nums1Map = {}
        for num in nums1:
            nums1Map[num] = 1 if num not in nums1Map else nums1Map[num] + 1
        for num in nums2:
            if target - num in nums1Map:
                result += nums1Map[target - num]
        return result

solution = Solution()
# solution.fourSumCount(nums1=[1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]) # 2
# solution.fourSumCount(nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]) # 1
solution.fourSumCount(
    nums1 = [39,87,-84,36,-20,88,-18,-50,18,12,51,8,79,18,-80,-62,54,26,-59,-95,-41,19,89,-95,45,-26,-15,6,-31,99,56,-94,-81,57,54,-42,-14,40,-12,-97,-82,25,50,-20,82,-55,-71,63,-70,-83,88,-1,-42,-88,-25,-49,-84,56,-55,-94,30,-15,87,-65,50,92,12,43,89,-95,-88,99,-3,-68,32,67,48,83,-11,-74,-87,-77,76,-79,-87,58,56,30,-53,97,-38,90,-39,-74,7,68,-10,61,95,73,94,77,-43,45,35,9,-18,18,79,76,14,-29,-27,-3,50,28,-69,-89,-15,-57,-22,-18,36,-61,66,-7,85,1,-84,-83,83,-53,-35,-27,43,-9,-14,-91,-3,16,-48,-82,-78,22,-97,25,4,-1,-45,35,34,-95,45,82,-100,-82,-44,-51,77,-82,-64,9,75,72,-78,35,14,2,-92,37,60,60,-62,-2,71,-66,-14,-81,-4,97,32,7,-32,88,-96,99,-18,88,-44],
    nums2 = [36,84,71,-90,23,-58,-59,-25,-37,-53,24,-28,32,-29,59,40,-96,23,70,53,10,-78,-31,48,-45,29,-8,61,36,5,-66,82,-97,20,-59,-50,68,-40,-75,98,-9,82,57,-47,90,53,-23,-42,100,-79,16,17,-93,-42,-57,-6,-97,-43,-49,90,-17,-41,51,61,85,-92,-24,-45,-46,53,-4,-64,-63,100,-50,-88,-87,29,13,-90,83,-98,-25,9,-56,52,-76,-17,14,99,-4,69,59,10,-67,-22,-49,-49,65,-73,-72,-3,12,100,-44,42,89,46,-71,-1,86,-87,46,-26,67,-66,-75,93,66,-65,-45,28,-62,-97,-27,-28,-83,67,16,-26,-91,-44,66,-78,-62,11,-10,-39,48,-100,47,-96,-42,-82,46,-27,9,53,-79,-18,44,-55,-76,91,-68,-4,82,-12,44,32,-1,-46,71,-80,49,-44,35,-57,-77,48,7,-50,15,92,16,17,45,29,-24,74,37,39,79,-23,48,72,-44,-1,1],
    nums3 = [-95,30,-76,-73,-40,-54,31,37,-42,82,-75,82,-4,-77,-78,-34,-50,-27,55,65,-83,75,-39,91,-34,-11,83,80,-52,22,80,-35,-93,-30,7,36,-96,-84,85,-94,13,27,-57,-81,-32,-67,-58,83,58,27,-35,44,-33,99,-98,-96,18,95,-88,97,8,23,-67,-96,66,-3,62,-51,2,49,-56,-63,-77,-60,95,82,11,17,-15,53,-62,63,75,91,45,83,-66,-59,-34,0,23,-21,-29,-42,-23,3,43,-98,89,-17,-26,-54,64,-17,-82,-20,-71,-88,-84,65,-97,29,17,-68,20,51,41,44,-55,-7,7,90,-84,66,-5,-14,73,23,65,-77,-80,-72,97,60,-88,34,48,-33,7,43,100,-4,72,72,-55,-28,60,-48,99,-43,3,-74,5,70,45,-3,-66,67,-87,67,34,-8,-6,-41,6,-34,39,-38,-58,44,-71,13,100,-77,-8,-54,-44,-96,90,79,-42,-57,52,99,-20,71,-60,91,-67],
    nums4 = [-91,63,-37,26,-87,-53,-58,-91,53,83,83,-43,66,22,-40,-49,-13,-22,23,-44,-97,40,-59,-28,-51,-59,52,58,-8,-31,-5,-4,-53,26,60,-60,42,55,71,-36,-7,4,-3,79,20,32,-19,48,-40,-30,48,-71,-94,100,21,59,14,69,-44,11,32,8,-95,-4,11,25,33,96,-23,56,-3,-42,60,-81,-40,48,20,-30,-21,-5,-95,-49,-33,-69,-78,83,-95,-65,-18,5,-73,-89,80,43,-54,-12,77,-79,-23,-93,-57,-78,58,-81,43,2,-50,-10,-4,-90,94,-15,-50,-12,21,-51,24,-45,-40,67,-44,21,-35,96,-63,94,-47,-72,4,-56,-49,43,-45,17,-63,-22,5,-19,22,51,41,-9,-45,100,3,65,61,59,9,-33,-67,-62,34,10,12,-51,-14,2,-68,-66,-82,56,84,-56,-68,-17,18,67,34,71,46,-29,-7,-85,31,95,84,-95,35,-26,65,70,-37,-83,-62,61,97,-89,45]
) # 4164554
solution.fourSumCount(
    nums1 = [100,4,16,-4,-78,92,80,-56,-23,57,88,28,-82,-41,28,17,48,-41,32,-17,29,84,-78,7,95,-59,-24,73,-76,-100,55,-39,36,-89,-72,11,-2,-86,-30,-88,47,-55,9,-46,50,-29,-13,-13,75,-28,41,-64,-68,12,-60,-4,-65,42,70,-25,100,38,49,6,22,-40,-66,-70,42,52,-41,51,81,12,-27,85,-40,17,93,-88,-34,76,97,-79,-71,-36,24,70,40,-1,63,24,20,50,-48,-85,71,31,37,-60,91,-68,67,20,47,-91,-20,25,60,98,59,-20,11,81,16,-29,-43,37,29,-22,-74,94,-43,83,93,-77,45,-100,-11,48,32,3,-44,43,-40,71,80,-14,38,88,-40,-17,65,-11,-87,90,94,99,50,-75,-27,-49,54,-97,8,-61,-51,-64,-81,88,3,77,-35,48,-19,41,-5,-88,5,-61,-27,7,-53,65,18,-19,-18,-6,29,60,-5,-39,-92,56,90,-46,-45],
    nums2 = [-49,-32,58,31,-78,-20,-96,72,93,83,79,-26,-54,9,-74,21,-14,44,-78,3,25,-23,97,34,61,4,53,-82,-70,-85,-2,-55,50,91,-60,-53,-5,-72,57,9,41,19,8,-92,-18,-77,39,-32,91,50,63,51,21,-65,-96,6,52,86,37,-50,-50,-33,-72,-37,-96,37,69,-25,54,-62,-83,-63,-4,-70,2,47,-85,27,92,-87,-81,2,-80,15,-73,-24,79,-37,91,-63,78,-88,-21,25,-72,82,15,33,51,88,26,-71,52,-61,-37,-37,21,67,35,-91,81,-70,57,65,-8,-22,-35,29,-16,-82,19,-22,-3,49,-42,-18,50,1,12,62,-47,68,-23,-67,-23,-37,31,4,65,37,55,90,93,94,66,-78,-19,-96,-31,-36,-79,95,-97,17,74,-5,6,-18,-88,-41,78,-86,55,-98,4,46,1,93,33,84,-55,-70,62,80,-14,-72,-11,-56,1,-20,100,67,100,16,-68,-46,37],
    nums3 = [-49,85,49,-79,-73,35,14,-55,-16,-1,59,-52,-51,4,-22,-77,-41,-78,28,-32,89,50,-58,27,-1,72,32,-24,93,1,-6,28,-81,68,-37,-65,34,65,-87,-48,-93,36,-52,64,59,-14,33,-62,77,-76,55,-12,34,77,65,-5,53,-27,-22,-57,-3,25,-85,23,58,-51,-97,-94,97,-20,53,-17,9,7,-79,-3,-69,-18,-63,69,2,100,45,-27,64,71,80,-52,100,-15,-63,83,36,-7,-74,-83,-52,76,43,28,-80,100,30,9,45,87,-39,98,6,28,-9,46,-20,-42,24,93,-13,27,-5,-18,31,4,0,-22,-16,-50,-63,-36,-92,-16,53,65,-31,-54,-48,-62,-80,41,66,-42,-90,52,-85,37,-12,52,-33,58,-58,52,-98,92,-46,-9,-67,49,45,-55,-37,-36,16,64,-85,-53,-75,59,-88,-77,-43,88,-32,-28,42,73,-37,-69,-7,55,23,-39,-11,-7,17,-69,-20,-38,-42],
    nums4 = [30,36,20,78,-9,-47,-41,-37,-2,-6,62,-97,-84,-87,-34,-52,-48,88,31,76,45,-49,-49,12,-93,-12,-22,-90,8,-44,41,37,23,-71,66,89,16,-40,41,-34,70,13,-89,-98,-34,86,-78,-92,-5,87,69,92,-87,-76,19,-25,-11,-12,41,-56,-98,-13,-26,65,12,-45,38,-90,32,81,-20,82,-70,49,38,89,53,63,41,8,44,79,25,70,37,-93,2,80,62,20,-1,34,53,25,-7,-8,95,14,-21,72,32,-39,83,-54,96,51,73,-51,-62,-18,-3,-58,40,-41,-78,-40,-22,-31,-11,-33,28,-69,-19,13,-98,90,97,68,13,-30,-75,-78,-28,28,-82,-75,-18,-41,75,75,41,0,67,75,92,62,45,-93,-3,-7,26,69,62,6,-93,-32,-61,-51,53,14,-41,-75,49,-14,-60,-14,-17,-89,-66,65,-50,41,-44,6,-29,-86,12,-79,-34,-55,-8,-11,83,22,67,90,96]
) # 4154227