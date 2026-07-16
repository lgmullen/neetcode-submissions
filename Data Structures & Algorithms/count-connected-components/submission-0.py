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
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
            return
        

        for i in range(0,n):
            if i not in visited:
                self.connected +=1
                dfs(i)
        return self.connected