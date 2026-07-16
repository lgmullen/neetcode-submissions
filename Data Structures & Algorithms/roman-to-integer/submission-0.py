class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        symbol_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M":1000
        }
        # iterate backwards
        for i in range(len(s)):
            # subtract current
            if i + 1 < len(s) and symbol_map[s[i+1]] > symbol_map[s[i]]:
                # subtract current i
                total -= symbol_map[s[i]]
            else:
                total += symbol_map[s[i]]

        return total