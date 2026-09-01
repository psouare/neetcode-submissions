class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r=0,len(s1)-1
        cs1=Counter(s1)
        while r<len(s2):
            sub=Counter(s2[l:r+1])

            if sub==cs1:
                return True
            r+=1
            l+=1
        
        return False

         
