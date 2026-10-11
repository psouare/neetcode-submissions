class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(len(edges)+1)]
        inDegree=[0]*(len(edges)+1)
        n=len(edges)
        q=deque()


        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            inDegree[u]+=1
            inDegree[v]+=1
        

        for i in range(n+1):
            if inDegree[i]==1:
                q.append(i)
        
        while q:
            a=q.popleft()
            inDegree[a]-=1
            for nei in adj[a]:
                inDegree[nei]-=1
                if inDegree[nei]==1:
                    q.append(nei)

                    
        for u,v in reversed(edges):
            if inDegree[u]==2 and inDegree[v]:
                return [u,v]
        

        return []



        



