class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pick=set()
        res=[]


        def dfs(subset,pick,cnt):
            if cnt==len(nums):
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if i not in pick:
                    pick.add(i)
                    subset.append(nums[i])
                    dfs(subset,pick,cnt+1)
                    subset.pop()
                    pick.remove(i)
            
        dfs([],pick,0)
        return res

        