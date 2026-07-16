class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.connected = 0
        adj = {}
        for i in range(n):
            adj[i] = []
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # this is what is visited
        visit = [False] * n
        def dfs(node):
            if visit[node] == True:
                return
            visit[node] = True
            for nei in adj[node]:
                dfs(nei)
            return
        

        for i in range(0,n):
            if visit[i] == False:
                self.connected +=1
                dfs(i)
        return self.connected