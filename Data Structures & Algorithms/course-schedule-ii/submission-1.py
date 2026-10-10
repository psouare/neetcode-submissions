class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q=deque()
        inDegree=[0]*numCourses
        adj=[[]for _ in range(numCourses)]

        for src,dest in prerequisites:
            inDegree[dest]+=1
            adj[src].append(dest)
        
        for i in range(numCourses):
            if inDegree[i]==0:
                q.append(i)

        
        finish=0
        output=[]
        while q:
            n=q.popleft()
            finish+=1
            output.append(n)
            for nei in adj[n]:
                inDegree[nei]-=1
                if inDegree[nei]==0:
                    q.append(nei)
        
        if finish!=numCourses:
            return []

        
        return output[::-1]
