class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=dict()
        d[nums[0]]=0
    
        

        for i in range(1,len(nums)):
            diff=target-nums[i]
            if diff in d :
                return [d[diff],i]
            d[nums[i]]=i

        

        

                