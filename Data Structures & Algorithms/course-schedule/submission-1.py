class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[]for _ in range(numCourses)]
        inDegree=[0]*numCourses
        q=deque()

        for src,dest in prerequisites:
            inDegree[dest]+=1
            adj[src].append(dest)

        for i in range(numCourses):
            if inDegree[i]==0:
                q.append(i)
        

        finish=0
        while q:
            n=q.popleft()
            finish+=1
            for nei in adj[n]:
                inDegree[nei]-=1
                if inDegree[nei]==0:
                    q.append(nei)
        
        return finish==numCourses



