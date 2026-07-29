class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        col = len(board[0])
        row = len(board)
        self.isTrue = False

        def dfs(i,j,sub, visited):
            if sub == word:
                self.isTrue = True
                return
            if i < 0 or j < 0 or i >= row or j >= col or len(sub) > len(word):
                return
            if (i,j) in visited:
                return
            
            visited.add((i,j))
            sub = sub + board[i][j]
            # ok now we can go 
            dfs(i+1,j,sub, visited)
            dfs(i-1,j,sub, visited)
            dfs(i,j+1,sub, visited)
            dfs(i,j-1,sub, visited)
            visited.remove((i,j))
            return
            
            





        # probs doesn't need to start until the word
        for i in range (0,len(board)):
            for j in range (0,len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    dfs(i,j,"", visited)
        return self.isTrue