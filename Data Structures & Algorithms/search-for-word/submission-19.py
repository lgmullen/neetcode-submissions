class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        col = len(board[0])
        row = len(board)
        self.isTrue = False

        def dfs(i,j,index, visited):
            if index == len(word):
                self.isTrue = True
                return True
            if i < 0 or j < 0 or i >= row or j >= col or word[index] != board[i][j]:
                return False
            if board[i][j] == "#":
                return False
            
            board[i][j] = "#"
            # ok now we can go 
            res = (dfs(i+1,j,index+1, visited) or
            dfs(i-1,j,index+1, visited) or 
            dfs(i,j+1,index+1, visited) or
            dfs(i,j-1,index+1, visited))
            # put it back
            board[i][j] = word[index]
            return res
            
            





        # probs doesn't need to start until the word
        for i in range (0,len(board)):
            for j in range (0,len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    dfs(i,j,0, visited)
        return self.isTrue