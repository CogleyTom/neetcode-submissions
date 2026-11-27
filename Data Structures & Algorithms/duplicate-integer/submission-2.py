class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = {}
        for number in nums:
            if number in mySet:
                mySet[number] += 1
            else:
                mySet[number] = 1
        return any(val > 1 for val in mySet.values())