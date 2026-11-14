class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for number in nums:
            if number in count:
                count[number] += 1
            else:
                count[number] = 1
        return max(count, key=count.get)
