class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]

        def dfs(total,subset,i):
            if total==target:
                res.append(subset.copy())
                return
            
            if i>=len(candidates) or total>target:
                return

            subset.append(candidates[i])
            total+=candidates[i]
            dfs(total,subset,i+1)
            subset.pop()
            total-=candidates[i]

            while i<len(candidates)-1 and  candidates[i]==candidates[i+1]:
                i+=1
                      
            dfs(total,subset,i+1)
        
        dfs(0,[],0)
        return res

        