class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            total = 0
            for digit in str(n):
                total += int(digit) ** 2
            n = total
            if n == 1:
                return True
        return False
        
        