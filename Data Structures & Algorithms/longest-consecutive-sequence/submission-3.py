class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count,maxcount=1,1
        if not nums:
            return 0

        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue

            elif nums[i]-nums[i-1]==1:
                count+=1
            else:
                maxcount=max(count,maxcount)
                count=1
        return max(count,maxcount)
