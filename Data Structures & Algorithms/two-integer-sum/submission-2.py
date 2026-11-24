class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mySet = {}
        for i, number in enumerate(nums):
            complement = target - number
            if complement in mySet:
                return [mySet[complement], i]
            mySet[number] = i