class Solution:
    def isValid(self, s: str) -> bool:

        closeD= {")":"(","}":"{","]":"["}
        stack=[]

        for c in s:
            if c in closeD:
                if stack and stack[-1]==closeD[c]:
                    stack.pop()
                
                else:
                    return False
            else:
                stack.append(c)
            
        
        return True if not stack else False
        