class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        
        for char in s:
            if char == "]":
                sub = ""
                while stack[-1] != "[":
                    cur = stack.pop()
                    sub = cur + sub
                # get the digits
                stack.pop()
                # here we need to get the digits
                mult = ""
                while stack and stack[-1].isdigit(): 
                    digit = stack.pop()
                    mult = digit + mult
                print(mult, sub)
                sub = int(mult) * sub
                stack.append(sub)
            else:

                stack.append(char)
        res = "".join(stack) 
        return res


            
        
