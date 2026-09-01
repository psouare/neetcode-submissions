class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges)>n-1:
            return False
        adj=[[] for _ in range(n)]
        visit=set()

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        def dfs(node, bef):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei==bef:
                    continue
                if not dfs(nei,node):
                    return False
            
            return True
            

        return dfs(0,-1) and len(visit)==n

        
        