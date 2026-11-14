class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        my_list = []
        my_list.extend(nums*2)
        return my_list