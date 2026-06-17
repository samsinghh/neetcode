class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(1, len(edges)+1)}
        visited = set()

        def dfs(node, par):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            
            visited.remove(node)
            return True
        
        for first, second in edges:
            adj[first].append(second)
            adj[second].append(first)

            if not dfs(first, -1):
                return [first, second]
        
        
            

        

        

        