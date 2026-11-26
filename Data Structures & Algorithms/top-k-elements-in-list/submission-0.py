class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myList = []
        myMap = {}
        for number in nums:
            if number in myMap:
                myMap[number] += 1
            else:
                myMap[number] = 1
        while k > 0:
            maxKey = max(myMap, key=myMap.get)
            myList.append(maxKey)
            myMap.pop(maxKey)
            k -= 1
        return myList
