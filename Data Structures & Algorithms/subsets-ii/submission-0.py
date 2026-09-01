class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()


        def dfs(result,i,subset):

            if i==len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(result,i+1,subset)    
            subset.pop()      
            while(i+1<len(nums) and nums[i]==nums[i+1]):
                i+=1
            
            dfs(result,i+1,subset)


        dfs(result,0,[])

        return result



            

