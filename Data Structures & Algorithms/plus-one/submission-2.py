class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits)-1
        carry = False
        while index >= 0 and digits[index] == 9:
            if index == 0:
                carry = True
            digits[index] = 0
            index -= 1
        if carry and digits:
            digits = [1] + digits
        else:
            digits[index] += 1
        return digits
        