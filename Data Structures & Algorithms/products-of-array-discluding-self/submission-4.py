class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftp=[1]*len(nums)
        rightp=[1]*len(nums)


        for i in range(len(nums)):
            if i==0:
                leftp[i]=nums[i]
            else:
                leftp[i]=leftp[i-1]*nums[i]

        for i in range(len(nums)-1,0,-1):
            if i==len(nums)-1:
                rightp[i]=nums[i]
            else:
                rightp[i]=rightp[i+1]*nums[i]


            

        res=[]

        for i in range(len(nums)):
            if i==0:
                res.append(rightp[i+1])

            elif i==len(nums)-1:
                res.append(leftp[i-1])
            
            else:
                res.append(rightp[i+1]*leftp[i-1])

        return res     

            
