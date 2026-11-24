class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = ''.join(char for char in s if char.isalnum()).lower()
        return cleanS == cleanS[::-1]