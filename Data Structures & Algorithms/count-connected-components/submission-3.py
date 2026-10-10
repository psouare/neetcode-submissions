class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        visit=set()
        cnt=0
        adj=[[]for _ in range(n)]


        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        def bfs(node):
            q=deque([node])
            while q:
                node=q.popleft()
                for nei in adj[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)

        for i in range(n):
            if i not in visit:
                visit.add(i)
                bfs(i)
                cnt+=1

        return cnt
        