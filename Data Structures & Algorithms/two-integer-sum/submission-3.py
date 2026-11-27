class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mySet = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in mySet:
                return [mySet[complement], i]
            mySet[n] = i