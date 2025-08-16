class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        stack,opens,closes=[],['(','[','{'],[')',']','}']
        for i in s:
            if i in opens:
                stack.append(i)
            if i in closes:
                if stack and closes.index(i)==opens.index(stack[-1]):
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        return False