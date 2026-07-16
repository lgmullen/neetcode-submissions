class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        def happy(n):
            if n in visited:
                return False
            visited.add(n)
            if n == 1:
                return True
            total = 0
            for digit in str(n):
                total += int(digit) ** 2
            return happy(total)
        return happy(n)
        