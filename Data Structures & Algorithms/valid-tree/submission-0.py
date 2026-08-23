class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        
        #create adj list
        for node,nei in edges:
            adj[node].append(nei)
            adj[nei].append(node)
        visited=set()

        def dfs(node,prev):
            if node in visited:
                return False
            visited.add(node)

            for i in adj[node]:
                if i ==prev:
                    continue 
                if not dfs(i,node):
                    return False
            return True
        
        return dfs(0,-1) and n==len(visited)

        