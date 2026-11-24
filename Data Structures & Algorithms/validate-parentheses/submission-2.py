class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        myMap = {')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in myMap:
                if myStack and myStack[-1] == myMap[char]:
                    myStack.pop()
                else:
                    return False
            else:
                myStack.append(char)
        return not myStack