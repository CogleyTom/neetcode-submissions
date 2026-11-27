class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            myMap[sortedS].append(s)
        return list(myMap.values())