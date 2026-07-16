class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        COLS = len(matrix[0])
        ROWS = len(matrix)
        res = [[0 for _ in range(ROWS)] for _ in range(COLS)]
        print(res)
        for r in range(ROWS):
            for c in range(COLS):
                res[c][r] = matrix[r][c]
        return res