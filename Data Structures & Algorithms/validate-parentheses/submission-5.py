class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        for char in s:
            if myStack and (char == '}' and myStack[-1] == '{'):
                myStack.pop()
            elif myStack and (char == ']' and myStack[-1] == '['):
                myStack.pop()
            elif myStack and (char == ')' and myStack[-1] == '('):
                myStack.pop()
            else:
                myStack.append(char)
        return not myStack
