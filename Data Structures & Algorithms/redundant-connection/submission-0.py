class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Number of edges.
        # In this problem, nodes are labeled from 1 to n.
        n = len(edges)

        # Adjacency list representing the graph built so far.
        # adj[node] contains all neighbors connected to `node`.
        adj = [[] for _ in range(n + 1)]

        def dfs(node, par):
            # If we reach a node we've already visited during
            # THIS DFS traversal, we've found a cycle.
            if visit[node]:
                return True

            # Mark this node as visited for the current DFS.
            visit[node] = True

            # Explore all neighbors connected to this node.
            for nei in adj[node]:

                # Since this is an undirected graph,
                # the node we just came from will appear as a neighbor.
                #
                # Example:
                # 1 --- 2
                #
                # If we go 1 -> 2, node 2 also sees node 1.
                # That's not a cycle, so skip the parent.
                if nei == par:
                    continue

                # Recursively explore this neighbor.
                # If any recursive call detects a cycle,
                # propagate True back up.
                if dfs(nei, node):
                    return True

            # Finished exploring this path and didn't find a cycle.
            return False

        # Add edges one at a time.
        for u, v in edges:

            # Add the new undirected edge:
            #
            # u <----> v
            adj[u].append(v)
            adj[v].append(u)

            # Reset visited before EACH new DFS.
            #
            # `visit` only represents nodes visited during
            # the CURRENT cycle check.
            #
            # We can't reuse the previous visit array because
            # those nodes were visited during an older DFS.
            visit = [False] * (n + 1)

            # After adding this edge, check whether the graph
            # now contains a cycle.
            #
            # Starting from `u` is enough because if the newly
            # added edge created a cycle, that cycle is inside
            # the connected component containing u and v.
            if dfs(u, -1):

                # The current edge is the one that caused the cycle,
                # so this is the redundant connection.
                return [u, v]

        # Problem guarantees there is a redundant edge,
        # but this is here as a fallback.
        return []