class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset=[]
        res=[]
        total=0

        def dfs(total,subset,i):
            if i==len(nums) and total!=target:
                return
            if total>target:
                return
            if total==target:
                res.append(subset.copy())
                return 
            subset.append(nums[i])
            total+=nums[i]
            dfs(total,subset,i)
            subset.pop()
            total-=nums[i]
            dfs(total,subset,i+1)

        dfs(0,[],0)
        return  res









        