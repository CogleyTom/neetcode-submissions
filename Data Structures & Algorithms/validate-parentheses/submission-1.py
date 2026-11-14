class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        for i, char in enumerate(s):
            if char == ']':
                if not myStack or myStack.pop() != '[':
                    return False
            elif char == ')':
                if not myStack or myStack.pop() != '(':
                    return False
            elif char == '}':
                if not myStack or myStack.pop() != '{':
                    return False
            else:
                myStack.append(char)
        return not myStack