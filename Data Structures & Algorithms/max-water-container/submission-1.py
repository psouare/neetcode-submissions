class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        maxrea=0
        while(l<r ):
            area=(r-l)*min(heights[l],heights[r])

            maxrea=max(maxrea,area)
        
            if heights[r]<heights[l]:
                r-=1
            else:
                l+=1
        

        return maxrea
        

        

            
            

        