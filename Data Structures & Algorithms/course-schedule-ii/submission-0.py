class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prem={i:[] for i in range(numCourses)}
        cycle,visit=set(),set()
        output=[]
        for c,p in prerequisites:
            prem[c].append(p)  
        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True
            cycle.add(c)
            for pre in prem[c]:
                if not dfs(pre) :
                    return False      
            cycle.remove(c)
            visit.add(c)
            output.append(c)
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return output

            


        
            
