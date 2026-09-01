class Solution:
    def findMin(self, nums: List[int]) -> int:

        l,r=0,len(nums)-1

        while l<r:
            k=(l+r)//2
            minK=nums[k]

            if nums[k]>nums[r]:
                l=k+1
            
            else:
                r=k
            
        return nums[l]
        