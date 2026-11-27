class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mySet = {}
        myList = []
        for number in nums:
            count = 0
            if number in mySet:
                mySet[number] += 1
            else:
                mySet[number] = 1
        for i in range(k):
            biggest = max(mySet, key=mySet.get)
            myList.append(biggest)
            mySet.pop(biggest)
        return myList