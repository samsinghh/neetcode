class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) > (n-1):
            return False

        adjacent = {i: [] for i in range(n)}
        for first, second in edges:
            adjacent[first].append(second)
            adjacent[second].append(first)
        
        visited, curr = set(), set()

        def dfs(v, prev):
            if v in visited:
                return True
            
            if v in curr:
                return False

            curr.add(v)
            for edge in adjacent[v]:
                if edge != prev:
                    if not dfs(edge, v):
                        return False
            
            curr.remove(v)
            visited.add(v)
            return True
        
        return dfs(n-1, -1) and len(visited) == n