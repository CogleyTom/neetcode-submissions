class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        orderS = ''.join(sorted(s))
        orderT = ''.join(sorted(t))
        if orderS == orderT:
            return True
        return False