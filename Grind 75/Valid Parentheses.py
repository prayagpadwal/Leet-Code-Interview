class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # creating a stack 
        check = {")":"(", "}":"{", "]":"["} # creating a dictionary 

        for c in s:
            if c in check:
                if stack and stack[-1] == check[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False