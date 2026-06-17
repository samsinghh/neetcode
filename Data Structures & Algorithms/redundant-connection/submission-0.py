class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(1, len(edges)+1)}

        def dfs(node, target, visited):
            if node == target:
                return True
            
            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True
            
            return False


        for u, v in edges:
            visited = set()
            if u in adj and v in adj and dfs(u, v, visited):
                return [u, v]
            
            adj[u].append(v)
            adj[v].append(u)
        
        return []
        

        