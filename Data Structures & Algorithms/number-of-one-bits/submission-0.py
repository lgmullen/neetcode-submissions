class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0
        binary = bin(n)
        for b in binary:
            if b == "1":
                num += 1
        return num