class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i, number in enumerate(nums):
            complement = target - number
            if complement in myMap:
                return [myMap[complement], i]
            myMap[number] = i