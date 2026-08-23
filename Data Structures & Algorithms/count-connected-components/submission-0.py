class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited=set()
        visits=0
        for node,nei in edges:
            adj[node].append(nei)
            adj[nei].append(node)
        
        def dfs(node):
            for i in adj[node]:
                if i in visited: continue
                else: 
                    visited.add(i)
                    dfs(i)
        
        for i in range(n):
            if i in visited:
                continue
            else:
                visited.add(i)
                dfs(i)
                visits+=1
        return visits
