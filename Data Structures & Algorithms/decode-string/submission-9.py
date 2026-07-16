class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        count_stack = []
        curr_string = ""
        curr_number = 0
        
        for char in s:
            if char == "[":
                stack.append(curr_string)
                count_stack.append(curr_number)
                curr_number = 0
                curr_string = ""
            elif char == "]":
                mult = count_stack.pop()
                sub = stack.pop()
                curr_string = sub + mult * curr_string
            elif char.isdigit():
                curr_number = curr_number * 10 + int(char)
            else:
                curr_string += char
        return curr_string


            
        
